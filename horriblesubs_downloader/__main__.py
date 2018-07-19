'''
HorribleSubs Downloader

Usage:
    hsd <name> <episode>

Options:
    -h --help   Show this screen.
'''

from docopt import docopt
import horriblesubs_downloader.scraper as scraper

def main():
    args = docopt(__doc__)

    # Usage: hsd <name> <episode>
    if args['<name>'] and args['<episode>']:
        name = args['<name>']
        episode = args['<episode>']
        print(scraper.getLink(name))

if __name__ == '__main__':
    main()
