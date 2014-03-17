#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用いよ．

python 010.py > data/010_out1.txt
sort data/col2.txt | uniq -c | sort -k 1 -r | cut -c 9- > data/010_out2.txt

"""

from __future__ import with_statement
from operator import itemgetter

def main():
    names = set()
    count = {}
    with open('./data/col2.txt') as f:
        for line in f:
            if line in names:
                count[line] += 1
                continue
            names.add(line)
            count[line] = 1
        for k, v in sorted(count.items(), key=itemgetter(1), reverse=True):
            print k,

if __name__ == '__main__':
    main()
