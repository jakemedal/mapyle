"""Methods and classes for watching files for
changes using watchdog
"""
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import watchdog

def event_response(event):
    print('hellaw')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = watchdog.events.PatternMatchingEventHandler(patterns=[".*.jpg"], ignore_patterns=[], ignore_directories=True)
    event_handler.on_any_event = event_response
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


