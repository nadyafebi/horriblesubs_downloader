'''
HorribleSubs Downloader

Usage:
    hsd <name> <episode> [(--to <path>)]
    hsd <name> --batch <start> <end> [(--to <path>)]
    hsd --config [<key>] [<value>]

Options:
    -h --help           Show this screen.
    -b --batch          Download multiple torrents.
    -c --config         Display or set config.
    -t --to <path>      Download file to path.
'''

from docopt import docopt
from horriblesubs_downloader.scraper import Scraper
from horriblesubs_downloader.downloader import Downloader
from horriblesubs_downloader.error import Error, DriverNotFound, DownloadPathNotSpecified
import configparser
import os, sys

def main():
    args = docopt(__doc__)

    browser = None
    try:
        # Open config
        config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
        config = configparser.ConfigParser()
        config.read(config_file)

        # Usage: hsd <name> <episode>
        #        hsd <name> --batch <start> <end>
        if args['<name>']:
            # Create anime info
            anime_info = {}
            anime_info['name'] = args['<name>']
            if args['<episode>']:
                anime_info['episodes'] = [int(args['<episode>'])]
            if args['--batch']:
                start = int(args['<start>'])
                end = int(args['<end>'])
                anime_info['episodes'] = range(start, end + 1)
            anime_info['resolution'] = 1080

            # Get driver
            try:
                driver = config['DEFAULT']['driver_path']
                if not driver:
                    raise DriverNotFound()
            except:
                raise DriverNotFound()

            # Create and open scraper
            scraper = Scraper(anime_info)
            sys.stdout.write('Opening browser...')
            sys.stdout.flush()
            scraper.openBrowser(driver)
            browser = scraper.browser

            # Get torrent link(s)
            print('Getting torrent link(s)...')
            links = scraper.getTorrent()
            anime_info['links'] = links

            # Download link(s)
            print('Downloading torrent file(s)...')
            downloader = Downloader(anime_info)
            try:
                destination = args['--to'] or config['DEFAULT']['download_path']
            except KeyError:
                raise DownloadPathNotSpecified()
            if not destination:
                raise DownloadPathNotSpecified()
            downloader.download(destination)

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

    except Error as e:
        print('ERROR:', e.msg)
        if e.help:
            print(e.help)
        if browser:
            browser.quit()
    except KeyboardInterrupt:
        if browser:
            browser.quit()
        print('Task canceled.')

if __name__ == '__main__':
    main()
