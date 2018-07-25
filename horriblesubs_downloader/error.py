class Error(Exception):
    def __init__(self, msg):
        self.msg = msg

class PageNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Page not found!')

class EpisodeNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Episode not found!')

class DriverNotFound(Error):
    def __init__(self):
        Error.__init__(self, 'Driver not found!')
