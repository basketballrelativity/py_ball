#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:41:34 2018

@author: patrickmcfarlane

setup.py

Standard setup.py script for the py_ball package.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_ball",
    version="1.0.1",
    author="Patrick McFarlane",
    author_email="patmcfarla@gmail.com",
    description="Python API wrapper for stats.nba.com with a focus on \
                 NBA and WNBA applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/basketballrelativity/py_ball",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
