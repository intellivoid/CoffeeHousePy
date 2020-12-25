import os
from setuptools import setup, find_packages

punkt_path = os.path.join('coffeehousemod_tokenizer', 'data')
punkt3_path = os.path.join('coffeehousemod_tokenizer', 'data', 'PY3')

punkt_files_fetch = os.listdir(os.path.join(os.getcwd(), punkt_path))
punkt_files = []
for file in punkt_files_fetch:
    file_path = os.path.join(os.getcwd(), punkt_path, file)
    if not os.path.isdir(file_path):
        punkt_files.append(file_path)

punkt3_files_fetch = os.listdir(os.path.join(os.getcwd(), punkt3_path))
punkt3_files = []
for file in punkt3_files_fetch:
    file_path = os.path.join(os.getcwd(), punkt3_path, file)
    if not os.path.isdir(file_path):
        punkt3_files.append(file_path)

setup(
    name='coffeehousemod_tokenizer',
    version='1.0.0',
    description='CoffeeHouseMod Punkt Data',
    url='https://github.com/Intellivoid/CoffeeHouseMod-Tokenizer',
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
        (os.path.join('coffeehousemod_tokenizer', 'data', 'tokenizers', 'punkt'), punkt_files),
        (os.path.join('coffeehousemod_tokenizer', 'data', 'tokenizers', 'punkt', 'PY3'), punkt3_files),
    ],
    keywords='nlp',
    packages=find_packages()
)
