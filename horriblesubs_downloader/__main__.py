'''
HorribleSubs Downloader

Usage:
    hsd <name> <episode>
    hsd <name> --batch <start> <end>
    hsd --config [<key>] [<value>]

Options:
    -h --help       Show this screen.
    -b --batch      Download multiple torrents.
    -c --config     Display or set config.
'''

from docopt import docopt
from horriblesubs_downloader.scraper import Scraper
from horriblesubs_downloader.error import Error, DriverNotFound
import configparser
import os, sys

def main():
    args = docopt(__doc__)

    # Open config
    config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_file)

    # Usage: hsd <name> <episode>
    #        hsd <name> --batch <start> <end>
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

        # Create scraper
        scraper = Scraper(anime_info)

        try:
            # Get driver
            try:
                driver = config['DEFAULT']['driver_path']
                if not driver:
                    raise DriverNotFound()
            except:
                raise DriverNotFound()

            # Open scraper
            sys.stdout.write('Opening browser...')
            sys.stdout.flush()
            scraper.openBrowser(driver)

            # Get torrent link(s)
            print('Getting torrent link(s)...')
            links = scraper.getTorrent()
            print(links)
        except Error as e:
            if scraper.browser:
                scraper.browser.quit()
            print('ERROR: ' + e.msg)
            if (e.help):
                print(e.help)

    # Usage: hsd --config [<key>] [<value>]
    if args['--config']:
        key = args['<key>']
        value = args['<value>']
        if key and value:
            config['DEFAULT'][key] = value
            config.write(open(config_file, 'w'))
        elif key:
            print(config['DEFAULT'][key])
        else:
            for key in config['DEFAULT']:
                print('{} = {}'.format(key, config['DEFAULT'][key]))

if __name__ == '__main__':
    main()
