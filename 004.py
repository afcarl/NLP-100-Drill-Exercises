#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""(4) (3)で作ったcol1.txtとcol2.txtを結合し，元のタブ区切りテキストを復元したもの．確認にはpasteコマンドを用いよ．

python 004.py
paste data/col1.txt data/col2.txt data/004_out2.txt
diff data/004_out1.txt data/004_out2.txt
"""

from __future__ import with_statement

def main():
    col1 = open('./data/col1.txt')
    col2 = open('./data/col2.txt')
    with open('./data/004_out.txt', 'w') as f:
        while True:
            try:
                f.write(col1.next().replace('\n', '\t') + col2.next())
            except StopIteration:
                break
    col1.close()
    col2.close()

if __name__ == '__main__':
    main()
