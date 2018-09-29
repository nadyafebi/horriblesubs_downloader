from setuptools import setup, find_packages

# Metadata
NAME = 'horriblesubs_downloader'
VERSION = '1.0'
DESCRIPTION = 'A simple anime torrent downloader.'
AUTHOR = 'Nadya Djojosantoso'
EMAIL = 'hello@nadyafebi.com'
URL = 'https://github.com/nadyafebi/horriblesubs_downloader'

# Packages
PACKAGES = find_packages(exclude=['*.tests'])
REQUIRED = [
    'docopt',
    'configparser',
    'clint',
    'selenium'
]

# CLI Settings
COMMAND = 'hsd'
ENTRY = {
    'console_scripts': ['{}={}.__main__:main'.format(COMMAND, NAME)]
}

# Get README
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# Magic begins here
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=PACKAGES,
    install_requires=REQUIRED,
    entry_points=ENTRY,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
