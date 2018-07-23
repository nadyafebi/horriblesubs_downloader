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
from horriblesubs_downloader.error import Error
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

        try:
            # Create scraper and open it
            scraper = Scraper(anime_info)
            sys.stdout.write('Opening browser...')
            sys.stdout.flush()
            scraper.openBrowser()

            # Get torrent link(s)
            print('Getting torrent link(s)...')
            links = scraper.getTorrent()
            print(links)
        except Error as e:
            scraper.browser.quit()
            print('ERROR: ' + e.msg)

if __name__ == '__main__':
    main()
