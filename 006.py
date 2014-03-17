#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(6) 自然数Nをコマンドライン引数にとり，入力のうち末尾のN行だけ．確認にはtailコマンドを用いよ．

python 006.py 5
tail -n 5 data/address.txt
"""

from __future__ import with_statement
import sys

def main():
    N = int(sys.argv[1])
    with open('./data/address.txt') as f:
        for line in list(f)[-N:]:
            print line,

if __name__ == '__main__':
    main()
