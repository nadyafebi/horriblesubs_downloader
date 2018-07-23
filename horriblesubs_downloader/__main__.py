'''
HorribleSubs Downloader

Usage:
    hsd <name> <episode>
    hsd <name> --batch <start> <end>

Options:
    -h --help   Show this screen.
'''

from docopt import docopt
from horriblesubs_downloader.scraper import Scraper
import sys

def main():
    args = docopt(__doc__)

    # Usage: hsd <name> <episode>
    if args['<name>']:
        # Add name to info
        anime_info = {}
        anime_info['name'] = args['<name>']

        # Add episodes to info
        if args['<episode>']:
            anime_info['episodes'] = [int(args['<episode>'])]
        if args['--batch']:
            start = int(args['<start>'])
            end = int(args['<end>'])
            anime_info['episodes'] = range(start, end + 1)

        # Add resolution to info
        anime_info['resolution'] = 1080

        # Create scraper and open it
        scraper = Scraper(anime_info)
        sys.stdout.write('Opening browser...')
        sys.stdout.flush()
        scraper.openBrowser()

        # Get torrent link(s)
        print('Getting torrent link(s)...')
        print(scraper.getTorrent())

if __name__ == '__main__':
    main()
