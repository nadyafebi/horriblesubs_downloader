'''
HorribleSubs Downloader

Usage:
    hsd <name> <episode>

Options:
    -h --help   Show this screen.
'''

from docopt import docopt

def main():
    args = docopt(__doc__)
    print(args['<name>'], args['<episode>'])

if __name__ == '__main__':
    main()
