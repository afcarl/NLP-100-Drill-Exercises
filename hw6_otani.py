#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""Solutions for exercises in juman_knp1.txt

Usage:
python hw6_otani.py <Q. number>
"""

import argparse
import logging
import sys
from pyknp import Juman, KNP

verbose = False
logger = None

def init_logger():
    global logger
    logger = logging.getLogger('Section1')
    logger.setLevel(logging.DEBUG)
    log_fmt = '%(asctime)s/%(name)s[%(levelname)s]: %(message)s'
    logging.basicConfig(format=log_fmt)

class Solver(object):
    def __init__(self):
        self.juman = Juman()
        self.knp = KNP()

    def Q61(self):
        u"""61. 文を標準入力から読み込み、それを単語単位に分かち書きせよ (形態素間にスペースを挿入)
        """

        input_sentence = raw_input()
        result = self.juman.analysis(input_sentence.decode('utf8'))
        for mrph in result.mrph_list():
            sys.stdout.write('{} '.format(mrph.midasi.encode('utf8')))
        sys.stdout.write('\n')
        return

    def Q62(self):
        u"""62. 形態素解析結果を読み込み、名詞だけを抽出してプリントせよ

        ヒント: mrph.hinsi が u"名詞" という文字列と一致するかどうかを判定
        """
        data = u''
        for line in iter(sys.stdin.readline, ""): # 入力文を1行ずつ読む
            data += line.decode('utf8')
            if line.strip() == 'EOS': # 1文が終わったら解析
                result = self.juman.result(data)
                s = ','.join(mrph.midasi for mrph in result.mrph_list()
                             if mrph.hinsi == u'名詞')  # 名詞だけ表示
                if len(s) > 0: print(s)
                data = u''


    def Q63(self):
        u"""62. 形態素解析結果を読み込み、名詞だけを抽出してプリントせよ

        ヒント: mrph.hinsi が u"名詞" という文字列と一致するかどうかを判定
        """
        data = u''
        for line in iter(sys.stdin.readline, ""): # 入力文を1行ずつ読む
            data += line.decode('utf8')
            if line.strip() == 'EOS': # 1文が終わったら解析
                result = self.juman.result(data)
                s = ','.join(mrph.genkei for mrph in result.mrph_list()
                             if mrph.hinsi == u'動詞')  # 動詞だけ表示
                if len(s) > 0: print(s)
                data = u''

    def Q64(self):
        u"""64. 形態素解析結果を読み込み、形態素の原形を頻度順に並べよ

        ヒント: ディクショナリ、sorted 関数を使う
        """
        data = u''
        hist = {}
        for line in iter(sys.stdin.readline, ""): # 入力文を1行ずつ読む
            data += line.decode('utf8')
            if line.strip() == 'EOS': # 1文が終わったら解析
                result = self.juman.result(data)
                for mrph in result.mrph_list():
                    try:
                        hist[mrph.genkei] += 1
                    except KeyError:
                        hist[mrph.genkei] = 1
                data = u''
        for key, val in sorted(hist.items(), key=lambda t:t[1], reverse=True):
            print('{},{}'.format(key.encode('utf8'), val))

    def Q65(self):
        u"""65. 形態素解析結果を読み込み、全形態素数 (総数) に対する述語の割合を計算せよ

        ここで、述語とは、動詞、イ形容詞 (形容詞)、ナ形容詞 (形容動詞) とする
        """

        data = u''
        num = 0
        denom = 0
        for line in iter(sys.stdin.readline, ""): # 入力文を1行ずつ読む
            data += line.decode('utf8')
            if line.strip() == 'EOS': # 1文が終わったら解析
                result = self.juman.result(data)
                if verbose: logger.info('denom: {}'.format(denom))
                for mrph in result.mrph_list():
                    denom += 1
                    if mrph.hinsi == u'動詞':
                        num += 1
                        continue
                    if mrph.hinsi == u'形容詞' and mrph.bunrui.startswith(u'イ形容詞'):
                        num += 1
                        continue
                    if mrph.hinsi == u'形容動詞' and mrph.bunrui.startswith(u'ナ形容詞'):
                        num += 1
                        continue
                data = u''

        print('{}/{}={}'.format(num, denom, float(num)/denom))

    def Q66(self):
        u"""66. 形態素解析結果を読み込み、「サ変名詞+する/できる」というパターンを抽出しプリントせよ
        """

        data = u''
        extract = set()
        for line in iter(sys.stdin.readline, ""): # 入力文を1行ずつ読む
            data += line.decode('utf8')
            if line.strip() == 'EOS': # 1文が終わったら解析
                result = self.juman.result(data)
                buff = None
                for mrph in result.mrph_list():
                    if mrph.genkei == u'できる' or mrph.genkei == u'する':
                        if buff is not None:
                            extract.add((buff.genkei.encode('utf8'), mrph.genkei.encode('utf8')))

                    if mrph.bunrui == u'サ変名詞':
                        buff = mrph
                    else:
                        buff = None
                data = u''
        for t in extract:
            print('{}+{}'.format(t[0], t[1]))

    def Q67(self):
        u"""67. 形態素解析結果を読み込み、「AのB」という表現 (A と B は名詞の1形態素) をすべてプリントせよ
        """

        data = u''
        extract = set()
        for line in iter(sys.stdin.readline, ""): # 入力文を1行ずつ読む
            data += line.decode('utf8')
            if line.strip() == 'EOS': # 1文が終わったら解析
                result = self.juman.result(data)
                buff = []
                for mrph in result.mrph_list():
                    if mrph.genkei == u'の' and len(buff) == 1:
                        buff.append(u'の')
                        continue
                    if mrph.hinsi == u'名詞':
                        if len(buff) == 0:
                            buff.append(mrph.genkei)
                            continue
                        if len(buff) == 2:
                            extract.add((buff[0], mrph.genkei))
                    buff = []
                data = u''
        for t in extract:
            print('{}の{}'.format(t[0].encode('utf8'), t[1].encode('utf8')))

    def Q68(self):
        u"""68. 文を標準入力から読み込み、それを文節単位に分かち書きせよ (文節間にスペースを挿入)
        """

        input_sentence = raw_input()
        result = self.knp.parse(input_sentence.decode('utf8'))
        for bnst in result.bnst_list():
            sys.stdout.write('{} '.format("".join(mrph.midasi.encode('utf8') for mrph in bnst.mrph_list())))
        sys.stdout.write('\n')
        return

    def Q69(self):
        u"""69. 構文解析結果を読み込み、接頭辞を含む文節をプリントせよ
        """

        data = u''
        extract = set()
        for line in iter(sys.stdin.readline, ""):
            data += line.decode('utf8')
            if line.strip() == 'EOS':
                result = self.knp.result(data)
                for bnst in result.bnst_list():
                    if len(filter(lambda x: x.hinsi == u'接頭辞', bnst.mrph_list())) < 1:
                        continue
                    extract.add('{} '.format("".join(mrph.midasi.encode('utf8') for mrph in bnst.mrph_list())))
                data = u''
        for bnst in extract:
            if len(bnst) > 0:
                print(bnst)
        return

    def Q70(self):
        u"""70. 構文解析結果を読み込み、名詞を2つ以上含む文節をプリントせよ
        """

        data = u''
        extract = set()
        for line in iter(sys.stdin.readline, ""):
            data += line.decode('utf8')
            if line.strip() == 'EOS':
                result = self.knp.result(data)
                for bnst in result.bnst_list():
                    if len(filter(lambda x: x.hinsi == u'名詞', bnst.mrph_list())) < 2:
                        continue
                    extract.add('{} '.format("".join(mrph.midasi.encode('utf8') for mrph in bnst.mrph_list())))
                data = u''
        for bnst in extract:
            if len(bnst) > 0:
                print(bnst)

        return

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
