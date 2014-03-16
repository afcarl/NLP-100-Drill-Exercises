#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(2) タブ１文字につきスペース１文字に置換したもの．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

python 002.py > data/002_out1.txt
sed "s/\t/　/g" data/address.txt > data/002_out2.txt
diff data/002_out1.txt data/002_out2.txt

"""

from __future__ import with_statement

def main():
    with open('./data/address.txt') as f:
        for line in f:
            print line.replace('\t', '　'),

if __name__ == '__main__':
    main()
