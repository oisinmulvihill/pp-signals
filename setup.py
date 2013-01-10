# -*- coding: utf-8 -*-
"""
Setuptools script for pp-signals (pp.signals)

"""

from setuptools import setup, find_packages

Name = 'pp-signals'
ProjectUrl = ""
Version = "1.0.1dev"
Author = ''
AuthorEmail = 'everyone at pythonpro dot co dot uk'
Maintainer = ''
Summary = ' pp-signals '
License = ''
Description = Summary
ShortDescription = Summary

needed = [
    'cmdln',
    'redis'
]

test_needed = [
]

test_suite = 'pp.signals.tests'

EagerResources = [
    'pp',
]

# Example including shell script out of scripts dir
ProjectScripts = [
]

PackageData = {
    '': ['*.*'],
}

# Example console script and paster template integration:
EntryPoints = {
    'console_scripts': [
        'signal-admin = pp.signals.scripts.main:main',
    ],
}


setup(
    url=ProjectUrl,
    name=Name,
    zip_safe=False,
    version=Version,
    author=Author,
    author_email=AuthorEmail,
    description=ShortDescription,
    long_description=Description,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    license=License,
    scripts=ProjectScripts,
    install_requires=needed,
    tests_require=test_needed,
    test_suite=test_suite,
    include_package_data=True,
    packages=find_packages(),
    package_data=PackageData,
    eager_resources=EagerResources,
    entry_points=EntryPoints,
    namespace_packages=['pp'],
)
