#!/usr/bin/env python

from setuptools import setup

setup(
    name='django_coverage_plugin',
    version='0.2',
    description='Django template coverage.py plugin',
    author='Ned Batchelder',
    author_email='ned@nedbatchelder.com',
    url='https://github.com/nedbat/django_coverage_plugin',
    packages=['django_coverage_plugin'],
    install_requires=[
        # If you change this, update tox.ini and requirements.txt also.
        'Django',
        'coverage >= 4.0a2',
        'six >= 1.4.0',
    ],
)
