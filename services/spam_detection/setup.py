from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        from resource_fetch import ResourceFetch
        rf = ResourceFetch()

        # Update the model
        rf.fetch("Intellivoid", "CoffeeHouseData-Spam")
setup(
    name='coffeehouse_spamdetection',
    version='1.0.0',
    description='Predicts input to be either spam or ham',
    url='https://github.com/Intellivoid/CoffeeHouse-SpamDetection',
    author='Zi Xing Narrakas',
    author_email='netkas@intellivoid.info',
    classifiers=[
        'Development Status :: 3 - Internal/Alpha',
        'Topic :: Text Processing',
        'Programming Language :: Python :: 3',
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    packages=find_packages()
)
