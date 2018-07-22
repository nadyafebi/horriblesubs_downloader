'''
HorribleSubs Downloader

Usage:
    hsd <name> <episode>
    hsd <name> --batch <start> <end>

Options:
    -h --help   Show this screen.
'''

from docopt import docopt
import horriblesubs_downloader.scraper as scraper

def main():
    args = docopt(__doc__)

    # Usage: hsd <name> <episode>
    if args['<name>']:
        name = args['<name>']
        if args['<episode>']:
            episode = int(args['<episode>'])
            print(scraper.getTorrent(name, [episode]))
        if args['--batch']:
            start = int(args['<start>'])
            end = int(args['<end>'])
            episodes = range(start, end + 1)
            print(scraper.getTorrent(name, episodes))

if __name__ == '__main__':
    main()
