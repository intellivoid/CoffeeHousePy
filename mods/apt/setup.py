import os
from setuptools import setup, find_packages

apt_file_path = os.path.join('coffeehousemod_apt', 'data')

apt_files_fetch = os.listdir(os.path.join(os.getcwd(), apt_file_path))
apt_files = []
for file in apt_files_fetch:
    file_path = os.path.join(os.getcwd(), apt_file_path, file)
    if not os.path.isdir(file_path):
        apt_files.append(file_path)

setup(
    name='coffeehousemod_apt',
    version='1.0.0',
    description='CoffeeHouseMod Averaged Perceptron Tagger',
    url='https://github.com/Intellivoid/CoffeeHouseMod-StopWords',
    author='Zi Xing Narrakas',
    author_email='netkas@intellivoid.info',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: Production/Stable - 5',
        'Topic :: API Wrapper',
        'Programming Language :: Python :: 3',
    ],
    data_files=[
        (os.path.join('coffeehousemod_apt', 'data', 'taggers', 'averaged_perceptron_tagger'), apt_files)
    ],
    keywords='nlp',
    packages=find_packages()
)
