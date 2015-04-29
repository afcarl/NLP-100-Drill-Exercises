#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""26. 強調マークアップの除去

25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
"""

import re
from p020 import load_data
from p025 import extract_basic_info

def remove_emphasis(text):
    for i in [5, 3, 2]:
        r = re.compile(r'(?:{emp}(?P<text{i}>\S*){emp})'.format(emp = '\'' * i, i=i))
        length = len(text)
        text = r.sub('\g<text{i}>'.format(i=i), text)
        if len(text) != length: return text  # updated
    return text


def main():
    data = load_data()
    info = extract_basic_info(data)

    # # Tests 
    # print(remove_emphasis("'''''aiueo'''''"))
    # print(remove_emphasis("''''aiueo''''"))
    # print(remove_emphasis("'''aiueo'''"))
    # print(remove_emphasis("''aiueo''"))
    # print(remove_emphasis("'aiueo'"))

    for key, val in info.items():
        print('key = {}'.format(key.encode('utf8')))
        print('value = {}\n'.format(remove_emphasis(val).encode('utf8')))
    return 0


if __name__ == '__main__':
    main()
