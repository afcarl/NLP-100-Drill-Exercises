#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(1) 行数をカウントしたもの．確認にはwcコマンドを用いよ．"""

from __future__ import with_statement

def main():
    with open('./data/address.txt') as f:
        print sum(1 for line in f)

if __name__ == '__main__':
    main()
