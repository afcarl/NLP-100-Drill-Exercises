#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""25. テンプレートの抽出

記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

import re
from p020 import load_data

def extract_basic_info(data):
    # Extract a subtext starting with {{基礎情報 and ending with }}
    r = re.compile(u'{{基礎情報 [^\n]*')
    m = r.search(data)
    start_pos = m.end()
    r = re.compile(r'}}\n')
    m = r.search(data[start_pos:])
    end_pos = m.start()

    result = {}
    for item in data[start_pos:][:end_pos].split('\n|'):
        r = re.compile(r'^(?P<key>[^=]+) = (?P<val>.+)', re.DOTALL)
        m = r.match(item.strip())
        if m is None: continue
        result[m.group('key').strip()] = m.group('val').strip()

    return result

def main():
    data = load_data()
    result = extract_basic_info(data)

    for key, val in result.items():
        print('key = {}'.format(key.encode('utf8')))
        print('value = {}\n'.format(val.encode('utf8')))
    return 0


if __name__ == '__main__':
    main()
