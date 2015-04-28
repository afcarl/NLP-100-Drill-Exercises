#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""Solutions for Section1
"""

import argparse
import logging
import random

verbose = False
logger = None

def init_logger():
    global logger
    logger = logging.getLogger('Section1')
    logger.setLevel(logging.DEBUG)
    log_fmt = '%(asctime)s/%(name)s[%(levelname)s]: %(message)s'
    logging.basicConfig(format=log_fmt)

class Solver(object):
    def Q00(self):
        u"""00. 文字列の逆順

        文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
        """

        answer = "stressed"[::-1]
        print(answer)
        return answer

    def Q01(self):
        u"""01. 「パタトクカシーー」

        「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
        """
        text = u"パタトクカシーー"
        answer = ''.join([text[i] for i in [0, 2, 4, 6]])
        print(answer)
        return answer

    def Q02(self):
        u"""02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

        「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
        """
        a = u"パトカー"
        b = u"タクシー"
        answer = ''.join([a[i] + b[i] for i in range(len(a))])
        print(answer)
        return answer

    def Q03(self):
        u"""03. 円周率

        "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から順に並べたリストを作成せよ．
        """
        text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        answer = map(lambda w: len(w), text[:-1].split())  # Discard the last period
        print(answer)
        return answer

    def Q04(self):
        u"""04. 元素記号

        "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型）を作成せよ．

        # 単語の位置は1から数え始めることにする
        """
        text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        usefirst = set([1, 5, 6, 7, 8, 9, 15, 16, 19])

        answer = {}
        pos = 0  # Record character position
        for i, word in enumerate(text.split(), start=1):
            k = ''
            if i in usefirst:
                k = word[0]
            else:
                k = word[:2]
            answer[k] = pos + 1
            pos += len(word) + 1

        print(answer)
        return answer


    def Q05(self):
        u"""05. n-gram

        与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

        # Includes spaces
        """

        def get_ngram(elements, n=2):
            l = []
            for i in range(len(elements)-1):
                l.append((elements[i], elements[i+1]))
            return set(l)

        text = "I am an NLPer"
        words_bigram = get_ngram(text.split())
        chars_bigram = get_ngram(text)
        print(words_bigram)
        print(chars_bigram)
        return words_bigram, chars_bigram


    def Q06(self):
        u"""06. 集合

        "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，補集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
        """

        def get_ngram(elements, n=2):
            l = []
            for i in range(len(elements)-1):
                l.append((elements[i], elements[i+1]))
            return set(l)

        textA = "paraparaparadise"
        textB = "paragraph"

        bigramA = get_ngram(textA)
        bigramB = get_ngram(textB)

        union = bigramA.union(bigramB)
        prod = bigramA.intersection(bigramB)
        comp = bigramA.difference(bigramB)
        flag = ('s', 'e') in prod

        print(union)
        print(prod)
        print(comp)
        print(flag)
        return union, prod, comp, flag


    def Q07(self):
        u"""07. テンプレートによる文生成

        引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
        """

        def gen_sentence(x, y, z):
            return u"{x}時の{y}は{z}".format(x=x, y=y, z=z)

        result = gen_sentence(12, u"気温", 22.4)

        print(result)
        return result


    def Q08(self):
        u"""08. 暗号文

        与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
        英小文字ならば(219 - 文字コード)の文字に置換
        その他の文字はそのまま出力
        この関数を用い，英語のメッセージを暗号化・復号化せよ．
        """
        def cipher(s):
           t = ''
           for c in s:
               if ord('a') <= ord(c) <= ord('z'):
                   t += chr(219 - ord(c))
                   continue
               t += c
           return t

        def decode(s):
           t = ''
           for c in s:
               if ord('a') <= 219 - ord(c) <= ord('z'):
                   t += chr(219 - ord(c))
                   continue
               t += c
           return t

        a = 'Hello, World!123'
        print('Original: ' + a)
        b = cipher(a)
        print('Encoded: ' + b)
        c = decode(b)
        print('Decoded: ' + c)

        return a, b, c


    def Q09(self):
        u"""09. Typoglycemia

        スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．

        # Let random seed = 1
        # Use "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        """
        random.seed(1)
        text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

        t = []
        for word in text.split():
            tail = ''
            if word[-1] in set(['.', ',']):  # Skip the last period and comma
                tail = word[-1]
                word = word[:-1]
            if len(word) > 4:  # Shuffle
                med = list(word[1:-1])  # Transform a string into a list
                random.shuffle(med)  # Shuffle elements in list
                word = word[0] + ''.join(med) + word[-1]  # Re-transform a list into a string
            t.append(word + tail)

        result = ' '.join(t) + '.'
        print(result)
        return result



def main(args):
    global verbose
    verbose = args.verbose

    solver = Solver()
    try:
        func = getattr(solver, 'Q{0:0>2}'.format(args.number))
    except AttributeError:
        logger.error('Invalid Question Number')
        return -1
    func()

    return 0


if __name__ == '__main__':
    init_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument('number')
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    args = parser.parse_args()
    main(args)
