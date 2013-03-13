import sys
import os
import BaseHTTPServer

def run(context_path='', port=9000):
    print 'starting local server!'
    # set current working dir on python path
    base_dir = os.path.normpath(os.path.abspath(os.path.curdir))
    sys.path.insert(0, base_dir)

    import handler
    import config

    handler.Handler.mappings = config.mappings

    server = BaseHTTPServer.HTTPServer((context_path, port), handler.Handler)

    server.serve_forever()