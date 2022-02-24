#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup.py - The core part of epub3.

Author: Matt Belfast Brown
E-mail: thedayofthedo@gmail.com
Create Date: 2022-02-23
Version Date: 2022-02-23
Version: 0.0.1

Copyright (C) 2022 Matt Belfast Brown
LICENSE　MIT LICENSE
"""

from setuptools import setup, find_packages

with open('ReadMe.md', 'r', encoding='utf-8') as dest_pimd:
    long_description = dest_pimd.read()

setup(
    name="epub3",
    version="0.0.1",

    author="Matt Belfast Brown",
    author_email="thedayofthedo@gmail.com",
    license="MIT LICENSE",

    description="Tool for epub3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["epub3", "pip", "HTML"],

    url="https://github.com/thedayofthedoctor/altl",
    project_urls={
        "Documentation": "http://belfast.web3v.work/program/doc/epub3/"
    },

    packages=find_packages(),
    py_modules=[],
    include_package_data=True,
    zip_safe=True,

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT LICENSE",
    ],
    platforms="any",
    install_requires=[],
    python_requires=">=3.6"
)
