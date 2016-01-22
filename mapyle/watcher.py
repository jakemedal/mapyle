"""Methods and classes for watching files for
changes using watchdog
"""
from watchdog.observers import Observer
from watchdog.events import FileModifiedEvent
from watchdog.events import FileCreatedEvent
from watchdog.events import PatternMatchingEventHandler

class SourceFileHandler(PatternMatchingEventHandler):
    def __super__(self, patterns=None, ignore_patterns=None, ignore_directories=False):
        """ TODO: pass an object that stores commands for each event
        call those commands on each event method
        """
        super.patterns = patterns
        super.ignore_directories = ignore_directories
        super.case_sensitive = True
        super.ignore_patterns = ignore_patterns

    def on_created(self, event):
        print('created')

    def on_modified(self, event):
        print('modified')

    def on_deleted(self, event):
        print('on_deleted')

    def on_moved(self, event):
        print('on_moved')

class FileWatcher():
    def __init__(self, path, filetypes, on_created, on_modified):
        self.path = path
        self.filetypes = filetypes
        self.observer = Observer()
        self.on_created = on_created
        self.on_modified = on_modified

    def start(self):
        event_handler = SourceFileHandler(patterns=self.filetypes, ignore_patterns=[], ignore_directories=True)

        # There are also 'on_deleted' and 'on_moved'

        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()
