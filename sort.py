from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os

class MyHandler(FileSystemEventHandler):
    print('Hi')
    i = 1
    def on_modified(self,event):
        print('hi1')
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            print(src,new_destination)
            os.rename(src, new_destination)
    print('hi2')

folder_destination = '/Users/Utkarsh GuptA/Desktop/IB/destination'
folder_to_track = '/Users/Utkarsh GuptA/Desktop/IB/source'
event_handler = MyHandler()
print('hi4')
observer = Observer()
print('hi5')
observer.schedule(event_handler, folder_to_track, recursive = True)
print('hi4=6')
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt():
    observer.stop()
observer.join()
