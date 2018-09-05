'''
HorribleSubs Downloader

Usage:
    hsd <name> <episode> [--res <res>] [(--to <path>)]
    hsd <name> --batch <start> <end> [--res <res>] [(--to <path>)]
    hsd --alias [<alias>] [<real>]
    hsd --config [<key>] [<value>]

Options:
    -h --help           Show this screen.
    -b --batch          Download multiple torrents.
    -r --res <res>      Set resolution.
    -t --to <path>      Download file to path.
    -a --alias          Set alias to an anime name.
    -c --config         Display or set config.
'''

from docopt import docopt
from horriblesubs_downloader.scraper import Scraper
from horriblesubs_downloader.downloader import Downloader
from horriblesubs_downloader.error import *
import configparser
from clint.textui import colored
from shutil import copyfile
import os, sys, time, threading, itertools

def main():
    args = docopt(__doc__)

    browser = None
    spinner = None
    try:
        # Open config
        config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
        if not os.path.isfile(config_file):
            config_template = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config-template.ini')
            copyfile(config_template, config_file)
        config = configparser.ConfigParser()
        config.read(config_file)

        # Usage: hsd <name> <episode>
        #        hsd <name> --batch <start> <end>
        if args['<name>']:
            # Get name
            anime_info = {}
            name = args['<name>']
            if name in config['ALIAS']:
                name = config['ALIAS'][name]
            anime_info['name'] = name

            # Get episode(s)
            try:
                if args['<episode>']:
                    anime_info['episodes'] = [int(args['<episode>'])]
                if args['--batch']:
                    start = int(args['<start>'])
                    end = int(args['<end>'])
                    anime_info['episodes'] = range(start, end + 1)
            except ValueError:
                raise EpisodeNumberInvalid()

            # Get resolution
            try:
                resolution = args['--res'] or config['CONFIG']['resolution']
                if not resolution:
                    raise ResolutionNotSpecified()
                resolution = int(resolution)
                if resolution not in [480, 720, 1080]:
                    raise ResolutionNumberInvalid()
            except ValueError:
                raise ResolutionNumberInvalid()
            except KeyError:
                raise ResolutionNotSpecified()
            anime_info['resolution'] = resolution

            # Get driver
            try:
                driver = config['CONFIG']['driver_path']
            except:
                raise DriverNotFound()
            if not driver:
                raise DriverNotFound()

            # Create and open scraper
            scraper = Scraper(anime_info)
            sys.stdout.write(colored.green('V') + ' ' + 'Opening browser...')
            sys.stdout.flush()
            scraper.createBrowser(driver)
            browser = scraper.browser

            spinner = Spinner('Opening page...')
            spinner.start()
            scraper.openBrowser()
            spinner.stop(True)

            # Get torrent link(s)
            spinner = Spinner('Getting torrent link(s)...')
            spinner.start()
            #print('Getting torrent link(s)...')
            links = scraper.getTorrent()
            anime_info['links'] = links
            spinner.stop(True)

            # Download link(s)
            spinner = Spinner('Downloading torrent file(s)...')
            spinner.start()
            downloader = Downloader(anime_info)
            try:
                destination = args['--to'] or config['CONFIG']['download_path']
            except KeyError:
                raise DownloadPathNotSpecified()
            if not destination:
                raise DownloadPathNotSpecified()
            downloader.download(destination)
            spinner.stop(True)

        # Usage: hsd --alias [<alias>] [<real>]
        if args['--alias']:
            alias = args['<alias>']
            real = args['<real>']
            if alias and real:
                config['ALIAS'][alias] = real
                config.write(open(config_file, 'w'))
            elif alias:
                print(config['ALIAS'][alias])
            else:
                for alias in config['ALIAS']:
                    print('{} = {}'.format(alias, config['ALIAS'][alias]))

        # Usage: hsd --config [<key>] [<value>]
        if args['--config']:
            key = args['<key>']
            value = args['<value>']
            if key and value:
                config['CONFIG'][key] = value
                config.write(open(config_file, 'w'))
            elif key:
                print(config['CONFIG'][key])
            else:
                for key in config['CONFIG']:
                    print('{} = {}'.format(key, config['CONFIG'][key]))

    except Error as e:
        if browser:
            browser.quit()
        if spinner:
            spinner.stop(False)
        print(colored.red('ERROR:'), e.msg)
        if e.help:
            print(e.help)
    except KeyboardInterrupt:
        if browser:
            browser.quit()
        if spinner:
            spinner.stop(False)
        print('Task canceled.')

class Spinner:
    spinner = itertools.cycle(['-', '/', '|', '\\'])

    def __init__(self, msg=None, delay=0.1):
        self.msg = msg
        self.delay = delay
        self.spinning = False

    def spin(self):
        while self.spinning:
            sys.stdout.write(colored.cyan(next(self.spinner)) + ' ' + self.msg)
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\r')
            sys.stdout.flush()

    def start(self):
        self.spinning = True
        threading.Thread(target=self.spin).start()

    def stop(self, success):
        self.spinning = False
        time.sleep(self.delay)
        if success:
            print(colored.green('V'), self.msg)
        else:
            print(colored.red('X'), self.msg)


if __name__ == '__main__':
    main()
