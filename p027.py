#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""26. 強調マークアップの除去

25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

import re
from p020 import load_data
from p025 import extract_basic_info
from p026 import remove_emphasis

def remove_internal_link(text):
    r = re.compile(r'\[\[.+\|(?P<name>.+?)\]\]')
    text = r.sub('\g<name>', text)
    r = re.compile(r'\[\[(?P<name>.+?)\]\]')
    return r.sub('\g<name>', text)

def main():
    data = load_data()
    info = extract_basic_info(data)

    for key, val in info.items():
        print('key = {}'.format(key.encode('utf8')))
        val = remove_emphasis(val)
        val = remove_internal_link(val)
        print('value = {}\n'.format(val.encode('utf8')))
    return 0


if __name__ == '__main__':
    main()
