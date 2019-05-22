#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.1.1'

with open('./README.md') as f:
    long_description = f.read()

setup(
    name='mc-uncertainty',
    version=version,
    author='Taylor Denouden',
    author_email='taylordenouden@gmail.com',
    packages=find_packages(),
    url='https://github.com/tayden/mc-uncertainty',
    license='MIT',
    description='Calculate uncertainty measures from Monte Carlo sampled model outputs.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy>=1.15.3",
    ],
)