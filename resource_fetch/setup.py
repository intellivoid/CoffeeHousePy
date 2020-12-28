from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='resource_fetch',
    version='1.0.0',
    description='Official CoffeeHouse API Wrapper for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['resource_fetch'],
    package_dir={
        'resource_fetch': 'resource_fetch'
    },
    author='Intellivoid Technologies',
    author_email='netkas@intellivoid.net',
    install_requires=[
        'packaging',
        'pygithub'
    ]
)
