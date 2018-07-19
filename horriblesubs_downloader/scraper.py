import re

HORRIBLE = 'https://horriblesubs.info/shows/'

def getLink(name):
    # Remove symbols
    name = re.sub(r'[^\w\s]', '', name)
    # Replace spaces with dash
    name = '-'.join(name.split())
    # Return HorribleSubs link
    return HORRIBLE + name
