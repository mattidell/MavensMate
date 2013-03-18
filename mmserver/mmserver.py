# -*- coding: utf-8 -*-
import argparse
import lib.server.server as server
import lib.server.server2 as server2
import lib.config as config
import threading

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mmpath') 
    args = parser.parse_args()
    config.mm_path = args.mmpath
    #server.run()
    server2.run()

if __name__ == '__main__':
    main() 