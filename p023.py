#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""23. セクション構造

記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import re
from p020 import load_data


def main():
    data = load_data()

    pat = r'(?P<sep>=+)(?P<title>[^=]+)=+\n'
    for m in re.finditer(pat, data):
        print('{},{}'.format(m.group('title').strip().encode('utf8'), len(m.group('sep'))))

    return 0


if __name__ == '__main__':
    main()
