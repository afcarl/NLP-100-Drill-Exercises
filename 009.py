#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(9) 各行を２コラム目，１コラム目の優先順位で辞書の逆順ソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．

python 009.py > data/009_out1.txt
sort -t '   ' -k 2 -r data/address.txt > data/009_out2.txt
"""

from __future__ import with_statement

def main():
    with open('./data/address.txt') as f:
        tuples = [cols[1] + '\t' + cols[0]
                  for cols in [line.split('\t')
                               for line in f]]
        for line in sorted(tuples, reverse=True):
            cols = line.split('\t')
            print cols[1] + '\t' + cols[0], #

if __name__ == '__main__':
    main()
