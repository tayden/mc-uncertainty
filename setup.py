#!/usr/bin/env python

from setuptools import setup, find_packages
import mc_uncertainty

setup(
    name='mc-uncertainty',
    version=mc_uncertainty.__version__,
    author='Taylor Denouden',
    author_email='taylordenouden@gmail.com',
    packages=find_packages(),
    url='https://github.com/tayden/mc-uncertainty',
    license='MIT',
    description='Calculate uncertainty measures from Monte Carlo sampled model outputs.',
    long_description=open('./README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy>=1.15.3",
    ],
)