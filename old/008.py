#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(8) 各行を２コラム目の辞書順にソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．

python 008.py > data/008_out1.txt
sort -t '   ' -k 2 data/address.txt > data/008_out2.txt
diff data/008_out1.txt data/008_out2.txt

"""

from __future__ import with_statement
from operator import itemgetter

def main():
    with open('./data/address.txt') as f:
        tuples = [tuple(line.split('\t')) for line in f]
        for line in sorted(tuples, key=itemgetter(1)):
            print '\t'.join(line), 

if __name__ == '__main__':
    main()
