# -*- coding: utf-8 -*-
import argparse
import lib.server.server_threaded as server_threaded
import lib.config as config
import threading

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mmpath') 
    args = parser.parse_args()
    config.mm_path = args.mmpath
    server_threaded.run()

if __name__ == '__main__':
    main() 