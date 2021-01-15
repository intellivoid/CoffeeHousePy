from setuptools import setup, find_packages
from setuptools.command.install import install


setup(
    name='coffeehouse_ping',
    version='1.0.0',
    description='Provides an endpoint for programs to ping for CoffeeHouse-Utils',
    url='https://github.com/Intellivoid/CoffeeHousePy',
    author='Zi Xing Narrakas',
    author_email='netkas@intellivoid.info',
    classifiers=[
        'Development Status :: 3 - Internal/Alpha'
    ],
    packages=find_packages()
)
