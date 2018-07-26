class Error(Exception):
    def __init__(self, msg, help=None):
        self.msg = msg
        self.help = help

class PageNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Page not found!')

class EpisodeNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Episode not found!')

class DriverNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Driver not found!', "To set driver, type 'hsd --config driver_path <PATH>'")
