#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""35. 名詞の連接

名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

from p030 import load_data

def extract_nounseries(data):
    result = set()
    for sent in data:
        buff = []
        for term in sent:
            # 名詞ならbuffに入れる
            if term[u'pos'] == u'名詞':
                buff.append(term[u'surface'])
                continue
            # 名詞でなく、かつbuffに何か入っていれば出力
            if len(buff) > 0:
                result.add(u''.join(buff))
            buff = []
    return result

def main():    
    data = load_data()

    nseries = extract_nounseries(data)
    # 結果の表示
    for ns in nseries:
        print(ns)

    return 0


if __name__ == '__main__':
    main()
