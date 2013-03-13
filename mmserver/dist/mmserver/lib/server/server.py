import sys
import os
import BaseHTTPServer
import handler
import config
import lib.config as global_config

server = None

def run(context_path='', port=9000):
    print 'starting local server!'
    # set current working dir on python path
    base_dir = os.path.normpath(os.path.abspath(os.path.curdir))
    sys.path.insert(0, base_dir)
    handler.Handler.mappings = config.mappings
    server = BaseHTTPServer.HTTPServer((context_path, port), handler.Handler)
    server.serve_forever()

def stop():
    print 'shutting down server'
    server.shutdown()