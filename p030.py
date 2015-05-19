#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""30. 形態素解析結果の読み込み

形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

def load_data(path='./data/neko.txt.mecab'):
    data = []
    with open(path) as f:
        l = []
        for buff in f:
            line = unicode(buff.strip(), 'utf8')
            if line == u'EOS':
                if len(l) > 0:
                    data.append(l)
                    l = []
                continue
            t1 = line.split('\t')
            dic = {}
            dic[u'surface'] = t1[0]
            t2 = t1[1].split(',')
            dic[u'base'] = t2[-3]
            dic[u'pos'] = t2[0]
            dic[u'pos1'] = t2[1]
            l.append(dic)
    return data

def main():    
    data = load_data()

    # 5文表示してみる
    for i in range(5):
        for t in data[i]:
            line = ''
            for key in [u'surface', u'base', u'pos', u'pos1']:
                line += u'{}: {}, '.format(key, t[key])
            print(line.encode('utf8'))
    return 0


if __name__ == '__main__':
    main()
