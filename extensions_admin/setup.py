#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='pulp_python_extensions_admin',
    version='0.0.0',
    packages=find_packages(),
    url='http://www.pulpproject.org',
    license='GPLv2+',
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    description='pulp-admin extensions for python package support',
    entry_points={
        'pulp.extensions.admin': [
            'repo_admin = pulp_python.extensions.admin.pulp_cli:initialize',
        ]
    }
)
