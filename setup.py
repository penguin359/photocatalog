from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='photocatalog',
    version='0.0.1',
    description='Python version of photo catalogging and GPS tracking software',
    long_description=long_description,
    url='https://github.com/penguin359/photocatalog',
    author='Loren M. Lang',
    author_email='lorenl@north-winds.org',
    license='BSD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['Django', 'lxml'],
    tests_require=['django-setuptest'],

    # django-setuptest test runner
    test_suite='setuptest.setuptest.SetupTestSuite',
)
