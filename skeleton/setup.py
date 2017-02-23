#!/usr/bin/python2.7
try:
	from setuptools import setup
except ImportError
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Zach Norgaard',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'znorgaar@fhcrc.org',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)
