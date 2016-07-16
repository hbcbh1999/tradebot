#!/usr/bin/python
from __future__ import print_function

import sys
import socket
import random
import time

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('test-exch-SEGFAULT', 20000))
    return s.makefile('w+', 1)

def main():
    exchange = connect()
    print('HELLO TEAMNAME', file=exchange)
    hello_from_exchange = exchange.readline().strip()
    print('The exchange replied:', hello_from_exchange, file=sys.stderr)
    id_no = 0
    while True:
    	print('ADD ' + str(id_no) + ' BOND BUY 995 100', file=exchange)
    	id_no += 1
        time.sleep(1)
        response = exchange.readline().strip()
    	print(response)

if __name__ == '__main__':
    main()
