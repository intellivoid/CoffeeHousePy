import os
import sys
import tarfile
import zipfile
from pathlib import Path
from packaging import version
from github import Github
from urllib.request import urlretrieve
from urllib.parse import urlparse


class ResourceFetch(object):

    def __init__(self):
        """
        ResourceFetch constructor
        """

        self.working_directory = os.path.join("/", "var", "resources")
        self.pat_path = os.path.join(self.working_directory, ".pat")
        self.github_client = None
        if not os.path.exists(self.working_directory):
            os.makedirs(self.working_directory)

    def rm(self, path):
        """
        Recursively removes a directory or file

        :param path:
        :return:
        """

        if os.path.isfile(path):
            os.remove(path)
            return

        directory = Path(path)
        for item in directory.iterdir():
            if item.is_dir():
                self.rm(item)
            else:
                item.unlink()
        directory.rmdir()

    def get_github(self):
        if self.github_client is None:
            self.github_client = Github(self.get_pat())
        return self.github_client

    def define_pat(self, token):
        """
        Defines/overwrites the personal access token for fetching resources

        :param token:
        :return:
        """

        if os.path.exists(self.pat_path):
            self.rm(self.pat_path)
        with open(self.pat_path, 'w+') as out:
            out.write(token)

    def get_pat(self):
        """
        Returns the personal access token that has been defined for fetching resources

        :return:
        """
        if not os.path.exists(self.pat_path):
            raise PermissionError("No Personal Access Token has been defined for ResourceFetcher")
        with open(self.pat_path, 'r') as file:
            return file.read()

    def fetch(self, organization, repository, check_for_update=True):
        """
        Fetches a resource, downloads it if it's missing and or updates it if it's outdated

        :param organization:
        :param repository:
        :param check_for_update:
        :return:
        """
        resource_path = os.path.join(self.working_directory, repository)

        if os.path.exists(resource_path):
            # The resource already exists, verify it

            if not check_for_update:  # Skip the check for updates
                return resource_path

            version_file = os.path.join(resource_path, ".version")
            with open(version_file, 'r') as file:
                current_version = file.read()

            # Check if it's outdated
            latest_version = self.get_latest_version(organization, repository)
            if version.parse(current_version) < version.parse(latest_version):
                self.install_resource(organization, repository, resource_path)
            return resource_path
        self.install_resource(organization, repository, resource_path)
        return resource_path

    def get_latest_version(self, organization, repository):
        """
        Returns the latest version of the resource

        :param organization:
        :param repository:
        :return:
        """
        releases = self.get_github().get_user(organization).get_repo(repository).get_releases()
        return releases[0].title

    def get_latest_download_url(self, organization, repository):
        """
        Gets the latest download URL for the requested resource

        :param organization:
        :param repository:
        :return:
        """

        releases = self.get_github().get_user(organization).get_repo(repository).get_releases()
        return releases[0].get_assets()[0].browser_download_url

    @staticmethod
    def reporthook(blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 1e2 / totalsize
            s = "\r%5.1f%% %*d / %d" % (
                percent, len(str(totalsize)), readsofar, totalsize)
            sys.stderr.write(s)
            if readsofar >= totalsize:  # near the end
                sys.stderr.write("\n")
        else:  # total size is unknown
            sys.stderr.write("read %d\n" % (readsofar,))

    def install_resource(self, organization, repository, path):
        print("Installing {0} from {1}".format(repository, organization))
        temporary_directory = os.path.join(self.working_directory, "tmp")
        if not os.path.exists(temporary_directory):
            os.makedirs(temporary_directory)

        # Prepare the download
        download_url = self.get_latest_download_url(organization, repository)
        parsed_url = urlparse(download_url)
        file_name = os.path.basename(parsed_url.path)
        file_path = os.path.join(temporary_directory, file_name)
        file_extension = os.path.splitext(file_name)[1]

        if os.path.exists(file_path):
            self.rm(file_path)

        if os.path.exists(path):
            self.rm(path)

        os.makedirs(path)
        urlretrieve(download_url, file_path, self.reporthook)

        print("Extracting archive")
        if file_name.endswith('.zip'):
            opener, mode = zipfile.ZipFile, 'r'
        elif file_name.endswith('.tar.gz') or file_name.endswith('.tgz'):
            opener, mode = tarfile.open, 'r:gz'
        elif file_name.endswith('.tar.bz2') or file_name.endswith('.tbz'):
            opener, mode = tarfile.open, 'r:bz2'
        else:
            raise ValueError("Could not extract `%s` as no appropriate extractor is found" % path)

        cwd = os.getcwd()
        os.chdir(path)

        try:
            file = opener(file_path, mode)
            try:
                file.extractall()
            finally:
                file.close()
        finally:
            os.chdir(cwd)

        with open(os.path.join(path, ".version"), 'w+') as out:
            out.write(self.get_latest_version(organization, repository))

        return True
