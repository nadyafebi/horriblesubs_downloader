# Base Error Class
class Error(Exception):
    def __init__(self, msg, help=None):
        self.msg = msg
        self.help = help

# MAIN ERRORS

class EpisodeNumberInvalid(Error):
    def __init__(self):
        Error.__init__(self, 'Episode number invalid!', 'Episode must be a positive integer.')

class ResolutionNumberInvalid(Error):
    def __init__(self):
        Error.__init__(self, 'Resolution number invalid!', 'Resolution must be 480/720/1080.')

class ResolutionNotSpecified(Error):
    def __init__(self):
        Error.__init__(self, 'Resolution not specified!', "Set resolution by adding '--res <RES>' at the end of the command or typing 'hsd --config resolution <RES>'")

class DownloadPathNotSpecified(Error):
    def __init__(self):
        Error.__init__(self, 'Download path not specified!', "Set path by adding '--to <PATH>' at the end of the command or typing 'hsd --config download_path <PATH>'")

# SCRAPER ERRORS

class PageNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Page not found!')

class EpisodeNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Episode not found!')

class DriverNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Driver not found!', "To set driver, type 'hsd --config driver_path <PATH>'")
