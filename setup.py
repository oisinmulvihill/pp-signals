# -*- coding: utf-8 -*-
"""
"""
from setuptools import setup, find_packages


Name = "pp-signals"
ProjectUrl = ""
Version = "1.0.2"
Author = 'Oisin Mulvihill'
AuthorEmail = 'oisin mulvihill at gmail'
Maintainer = 'PubSub in python using Redis for the subscribe and publish.'
Summary = 'Testing Helper Library.'
License = ''
Description = Summary
ShortDescription = Summary


needed = [
    "cmdln",
    "redis",
]

test_needed = [
    "pytest-cov",
]

test_suite = ''

EagerResources = [
    'pp',
]

ProjectScripts = [
]

PackageData = {
    '': ['*.*'],
}

EntryPoints = {
    'console_scripts': [
        'signal-admin = pp.signals.scripts.main:main'
    ]
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
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
    ],
    keywords='python',
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
