import os
from setuptools import setup, find_packages

stopwords_file_path = os.path.join('coffeehousemod_stopwords', 'data')

stopwords_files_fetch = os.listdir(os.path.join(os.getcwd(), stopwords_file_path))
stopwords_files = []
for file in stopwords_files_fetch:
    file_path = os.path.join(os.getcwd(), stopwords_file_path, file)
    if not os.path.isdir(file_path):
        stopwords_files.append(file_path)

setup(
    name='coffeehousemod_stopwords',
    version='1.0.0',
    description='CoffeeHouseMod StopWords Data',
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
        (os.path.join('coffeehousemod_stopwords', 'data', 'corpora', 'stopwords'), stopwords_files)
    ],
    keywords='nlp',
    packages=find_packages()
)
