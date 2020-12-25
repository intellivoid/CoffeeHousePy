from setuptools import setup, find_packages

setup(
    name='coffeehouse_alg',
    version='1.0.0',
    description='CoffeeHouse algorithmia wrapper',
    url='https://github.com/Intellivoid/CoffeeHouse-ALG',
    author='Zi Xing Narrakas',
    author_email='netkas@intellivoid.info',
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Topic :: API Wrapper',
        'Programming Language :: Python :: 3',
    ],
    keywords='multi-label classification nlp neural networks deep learning api wrapper',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests'
    ]
)
