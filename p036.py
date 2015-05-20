#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""36. 単語の出現頻度

文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

from p030 import load_data

def calc_word_freq(data, use_base=True):
    u"""出現頻度をカウント

    デフォルトでbaseを使う
    """
    counter = {}
    for sent in data:
        for term in sent:
            if use_base:
                key = term[u'base']
            else:
                key = term[u'surface']
            try:
                counter[key] += 1
            except KeyError:  # 初出の単語
                counter[key] = 1
    return counter

def main():    
    data = load_data()

    freq = calc_word_freq(data)
    # 結果の表示
    for key, val in sorted(freq.items(), key=lambda t:t[1], reverse=True):
        print('{}: {}'.format(key.encode('utf8'), val))

    return 0


if __name__ == '__main__':
    main()
