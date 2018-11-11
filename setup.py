#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = []
github_requirements = []
PACKAGE_NAME = 'loggable'
setup(
    name=PACKAGE_NAME,
    version='0.1.0',
    author="mvr",
    description="logging mixins and tools",
    author_email='no-reply@example.com',
    url='https://github.com/mattvonrocketstein/redditdb',
    packages=find_packages(),
    install_requires=requirements,
    dependency_links=github_requirements,
    zip_safe=False,
    entry_points={},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
