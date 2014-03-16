#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(5) 自然数Nをコマンドライン引数にとり，入力のうち先頭のN行だけ．確認にはheadコマンドを用いよ．"

python 005.py 5
head -n 5 data/address.txt
"""

from __future__ import with_statement
import sys

def main():
    N = int(sys.argv[1])
    with open('./data/address.txt') as f:
        for line in f:
            if N <= 0:
                break
            print line,
            N -= 1

if __name__ == '__main__':
    main()
