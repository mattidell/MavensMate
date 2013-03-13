#MavensMate.app will be launched 1 of 2 ways:
#1. by opening the app from Application directory (unlikely)
#2. when an operation is run from a MavensMate plugin, the plugin will check if MavensMate.app is running
#   and if it isn't it will start it. The local server should always start at main and should shut down when
#   the MavensMate process is killed
# -*- coding: utf-8 -*-
import argparse
import lib.server.server as server
from lib.server.daemon import Daemon
import lib.config as config
#import os
#print config.base_path

import threading
# class ServerThread(threading.Thread):
#     def __init__(self, num=0):
#         threading.Thread.__init__(self)
#         self.stop_event = threading.Event()
#         #self.running = True
#         self.num = num
        
#     def stop(self):
#         self.stop_event.set()
        
#     def run(self):
#         server.run()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mmpath') 
    args = parser.parse_args()
    config.mm_path = args.mmpath
    server.run()

if __name__ == '__main__':
    main()
    