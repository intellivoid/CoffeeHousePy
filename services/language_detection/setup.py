import os

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        from resource_fetch import ResourceFetch
        rf = ResourceFetch()

        # Update the model
        rf.fetch("Intellivoid", "CoffeeHouseData-LangDetect")


setup(
    name='coffeehouse_languagedetection',
    version='1.0.0',
    description='Multi-method Language Detection Library',
    url='https://github.com/Intellivoid/CoffeeHouse-LanguageDetection',
    author='Zi Xing Narrakas',
    author_email='netkas@intellivoid.net',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Text Processing',
        'Programming Language :: Python :: 3',
    ],
    keywords='machine learning language detection',
    install_requires=[
        'scikit-learn==0.22.0',
        'joblib',
        'six'
    ],
    data_files=[
        (
            os.path.join('coffeehouse_languagedetection', 'ldutils'),
            [os.path.join('coffeehouse_languagedetection', 'ldutils', 'messages.properties')]
        )
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    packages=find_packages()
)
