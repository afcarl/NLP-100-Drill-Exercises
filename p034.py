#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""34. 「AのB」

2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

from p030 import load_data

def extract_nounphrases(data):
    result = set()
    for sent in data:
        buff = []
        for term in sent:
            if term[u'surface'] == u'の':
                if len(buff) != 1:  # buffに名詞が1つも入っていないなら無視
                    buff = []
                    continue
                buff.append(u'の')
                continue
            if term[u'pos'] != u'名詞':  # 名詞でなければbuffを空にする
                buff = []
                continue
            if len(buff) == 2:  # <名詞>の
                buff.append(term[u'surface'])
                result.add(u''.join(buff))
            buff = [term[u'surface'],]
    return result

def main():    
    data = load_data()

    nphrases = extract_nounphrases(data)
    # 結果の表示
    for nphrase in nphrases:
        print(nphrase)
    # 3897 words
    return 0


if __name__ == '__main__':
    main()
