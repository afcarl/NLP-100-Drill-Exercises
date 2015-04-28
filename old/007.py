#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(7) １コラム目の文字列の異なり数（種類数）．確認にはcut, sort, uniq, wcコマンドを用いよ．

python 007.py
cut -f 1 data/address.txt| sort | uniq | wc
"""

from __future__ import with_statement

def main():
    pref = set()
    with open('./data/col1.txt') as f:
        for line in f:
            pref.add(line)
    print len(pref)

if __name__ == '__main__':
    main()
