from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='coffeehouse_translation',
    version='1.0.0',
    description='Translates inputs into different languages',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['coffeehouse_translation'],
    package_dir={
        'coffeehouse_translation': 'coffeehouse_translation'
    },
    author='Intellivoid Technologies',
    author_email='netkas@intellivoid.net',
    install_requires=[
        'googletrans'
    ]
)
