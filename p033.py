#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""33. サ変名詞

サ変接続の名詞をすべて抽出せよ．
"""

from p030 import load_data

def extract_sahensetsuzoku_nouns(data):
    result = set()
    for sent in data:
        for term in sent:
            if term[u'pos1'] == u'サ変接続':  # pos1がサ変接続ならposは名詞
                result.add(term[u'surface'])  # 表層形を抽出する
    return result

def main():    
    data = load_data()

    nouns = extract_sahensetsuzoku_nouns(data)
    # 結果の表示
    for noun in nouns:
        print(noun)
    # 3897 words
    return 0


if __name__ == '__main__':
    main()
