import time
from watcher import FileWatcher

def on_create():
    print('created file')

def on_modified():
    print('modified file')

watcher = FileWatcher('.', '*.jpg', on_create, on_modified)
watcher.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    watcher.stop()

