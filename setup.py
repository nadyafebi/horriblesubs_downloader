from setuptools import setup, find_packages

# Metadata
NAME = 'horriblesubs_downloader'
VERSION = ''
DESCRIPTION = ''
AUTHOR = 'Nadya Djojosantoso'
EMAIL = 'hello@nadyafebi.com'
URL = 'https://github.com/nadyafebi/horriblesubs_downloader'

# Packages
PACKAGES = find_packages(exclude=['*.tests'])
REQUIRED = [
    'docopt'
]

# CLI Settings
COMMAND = 'hsd'
ENTRY = {
    'console_scripts': ['{}={}.__main__:main'.format(COMMAND, NAME)]
}

# Magic begins here
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=PACKAGES,
    install_requires=REQUIRED,
    entry_points=ENTRY
)
