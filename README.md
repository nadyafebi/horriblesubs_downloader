# HorribleSubs Downloader

A simple anime torrent downloader.

**Features:**
* Quickly download anime torrents from HorribleSubs in your terminal.
* Download the whole season in a single command.
* Use alias for anime with long name.

*Note: The downloader doesn't work for older anime that has no torrent link. Support for magnet link will be added in the future.*

***

**Table of Contents**
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

***

## Installation

You need [Python 3.x.x](https://www.python.org/downloads/) to install and use the downloader.

```bash
pip install horriblesubs_downloader
```

1. Download [chromedriver](http://chromedriver.chromium.org/downloads) and extract out the file inside the ZIP.
1. Type in your terminal:<br>
  `hsd --config driver_path <PATH TO CHROMEDRIVER>`<br>
  Example:<br>
  `hsd --config driver_path 'C:\Users\me\Documents\chromedriver.exe'`<br>
1. Set your download path:<br>
  `hsd --config download_path <PATH>`<br>
  Example:<br>
  `hsd --config download_path 'C:\Users\me\Downloads\Torrent'`<br>
1. You're all set!

## Usage

```
Usage:
    hsd <name> <episode> [--res <res>] [--to <path>]
    hsd <name> <start> <end> [--res <res>] [--to <path>]
    hsd <name> --batch [--res <res>] [--to <path>]
    hsd --alias [<alias>] [<real>]
    hsd --config [<key>] [<value>]

Options:
    -h --help           Show this screen.
    -b --batch          Download multiple torrents.
    -r --res <res>      Set resolution.
    -t --to <path>      Download file to path.
    -a --alias          Display or set alias.
    -c --config         Display or set config.
```

**Examples**
```bash
# Download episode 5 of One Punch Man
hsd "One Punch Man" 5

# Download episode 1-3 of KonoSuba
hsd --alias "KonoSuba" "Kono Subarashii Sekai ni Shukufuku wo!"
hsd "KonoSuba" 1 3

# Download the whole season of Steins Gate in 720p
hsd "Steins Gate" --batch --res 720

# Display all aliases and config
hsd --alias
hsd --config
```

## License

[MIT License](https://github.com/nadyafebi/horriblesubs_downloader/blob/master/LICENSE)
