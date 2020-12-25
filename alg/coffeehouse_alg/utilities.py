import requests
import mimetypes
import base64
import re


class Utilities:

    @staticmethod
    def get_cookies(http_endpoint):
        """
        Makes the initial request to get all the required cookies

        :return: dict value of all the returned cookies
        """
        session = requests.Session()
        session.get(http_endpoint)
        return session.cookies.get_dict()

    @staticmethod
    def get_access_key(http_endpoint):
        """
        Sends a request to a Javascript content file and parses the contents
        to extract the access key (Simple)

        :param http_endpoint:
        :return:
        """
        response = requests.get(http_endpoint)
        access_key = re.findall('\'([^"]*)\'', response.text.splitlines()[1])[0]
        return "Simple {0}".format(access_key)

    @staticmethod
    def process_img_from_url(url):
        """
        Downloads the image from the URl and processes it into a proper
        base64 encoded image with the mime type information included

        :param url:
        :return:
        """
        mimetype = mimetypes.guess_type(url)[0]
        image_content = requests.get(url).content
        image_b64content = base64.b64encode(image_content).decode('utf8')
        return "data:%s;base64,%s" % (mimetype, image_b64content)

    @staticmethod
    def add_client_headers(headers):
        """
        Adds the required client headers
        :param headers:
        :return:
        """
        headers['Accept-Encoding'] = 'gzip, deflate, br'
        headers['Accept-Language'] = 'en'
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                'Chrome/80.0.3987.122 Safari/537.36 '
        return headers
