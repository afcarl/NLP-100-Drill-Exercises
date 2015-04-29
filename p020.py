#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""20. JSONデータの読み込み

Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import gzip
import json

def load_data():
    with gzip.open('data/jawiki-country.json.gz') as f:
        for line in f:
            data = json.loads(line.decode('utf8'))
            if data['title'] == u'イギリス':
                break
    return data['text']


def main():
    data = load_data()

    print(data.encode('utf8'))

    return 0


if __name__ == '__main__':
    main()
