#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""24. ファイル参照の抽出

記事から参照されているメディアファイルをすべて抜き出せ．
"""

import re
from p020 import load_data


def main():
    data = load_data()

    pat = r'[\[\[]?(?:ファイル|File):(?P<name>[^|]+)\|'
    for m in re.finditer(pat, data):
        print(m.group('name').encode('utf8'))

    return 0


if __name__ == '__main__':
    main()
