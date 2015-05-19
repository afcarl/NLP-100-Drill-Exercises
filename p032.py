#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""32. 動詞の原形

動詞の原形をすべて抽出せよ．
"""

from p030 import load_data

def extract_verbs_base(data):
    result = set()
    for sent in data:
        for term in sent:
            if term[u'pos'] == u'動詞':  # pos1がサ変接続ならposは名詞
                result.add(term[u'base'])
    return result

def main():    
    data = load_data()

    verbs = extract_verbs_base(data)
    # 結果の表示
    for verb in verbs:
        print(verb.encode('utf8'))
    # 3897 words
    return 0


if __name__ == '__main__':
    main()
