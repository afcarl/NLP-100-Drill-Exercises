#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""22. カテゴリ名の抽出

記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

import re
from p020 import load_data


def main():
    data = load_data()

    pat = r'\[\[Category:(?P<name>[^\]\|]*)\|*[^\]]*\]\]'
    for m in re.finditer(pat, data):
        print(m.group('name').encode('utf8'))

    return 0


if __name__ == '__main__':
    main()
