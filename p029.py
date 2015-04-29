#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""29. 国旗画像のURLを取得する

テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）"""

import json
import urllib
import re
from p020 import load_data
from p025 import extract_basic_info

def main():
    data = load_data()
    info = extract_basic_info(data)

    param = {
        'action': 'query',
        'format': 'json',
        'iiprop': 'url',
        'prop': 'imageinfo',
        'titles': 'Image:{}'.format(info[u'国旗画像'])
    }
    url = u'http://ja.wikipedia.org/w/api.php?' + urllib.urlencode(param)

    try:
        r = urllib.urlopen(url)
        data = json.loads(r.read().decode('utf8'))
        print(data[u'query'][u'pages'][u'-1'][u'imageinfo'][0][u'url'])
    finally:
        r.close()
    return 0


if __name__ == '__main__':
    main()
