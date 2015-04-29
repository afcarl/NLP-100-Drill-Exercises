#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""28. MediaWikiマークアップの除去

27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

import re
from p020 import load_data
from p025 import extract_basic_info
from p026 import remove_emphasis
from p027 import remove_internal_link

def remove_file_link(text):
    r = re.compile(u'^\[\[(?:ファイル|File):(?P<name>.+?)\|.+')
    return r.sub('\g<name>', text)

def remove_lang(text):
    r = re.compile(u'{{lang\|.+\|(?P<name>.+?)}}')
    return r.sub('\g<name>', text)

def remove_external_link(text):
    r = re.compile(r'\['
                   r'(?P<url>\S+)'
                   r'\s?'
                   r'(?P<name>.+?)?'
                   r'\]')
    m = r.search(text)
    if m is None:
        return text
    if m.group('name'):
        return m.group('name')
    return m.group('url')

def main():
    data = load_data()
    info = extract_basic_info(data)

    for key, val in info.items():
        print('key = {}'.format(key.encode('utf8')))
        val = remove_emphasis(val)
        val = remove_internal_link(val)
        val = remove_external_link(val)
        val = remove_file_link(val)
        val = remove_lang(val)
        print('value = {}\n'.format(val.encode('utf8')))
    return 0


if __name__ == '__main__':
    main()
