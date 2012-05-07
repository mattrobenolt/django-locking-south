#!/usr/bin/env python
"""
django-locking-south
======

Prevent South from running concurrently.
"""

from setuptools import setup, find_packages

install_requires = [
    'Django',
    'South',
]

setup(
    name='django-locking-south',
    version='0.1.0',
    description='Prevent South from running concurrently',
    long_description=__doc__,
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    packages=find_packages(),
    zip_safe=False,
    license='MIT',
    url='https://github.com/mattrobenolt/django-locking-south',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=install_requires,
)
