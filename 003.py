#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(3) 各行の１列目だけを抜き出したものをcol1.txtに，２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

python 003.py
cut -f 1 data/address.txt > data/col1_cut.txt
cut -f 2 data/address.txt > data/col2_cut.txt
diff data/col1.txt data/col1_cut.txt
diff data/col2.txt data/col2_cut.txt

"""

from __future__ import with_statement

def main():
    col1 = open('./data/col1.txt', 'w')
    col2 = open('./data/col2.txt', 'w')
    with open('./data/address.txt') as f:
        for line in f:
            c1, c2 = line.split('\t')
            col1.write(c1 + '\n')
            col2.write(c2)
    col1.close()
    col2.close()

if __name__ == '__main__':
    main()
