#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""21. カテゴリ名を含む行を抽出

記事中でカテゴリ名を宣言している行を抽出せよ．
"""

import re
from p020 import load_data


def main():
    data = load_data()

    pat = r'\[\[Category:[^\]]*\]\]'
    for m in re.finditer(pat, data):
        print(m.group().encode('utf8'))

    return 0


if __name__ == '__main__':
    main()
