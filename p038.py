#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""38. ヒストグラム

単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

from p030 import load_data
from p036 import calc_word_freq
import matplotlib.pyplot as plt


def main():    
    data = load_data()

    freq = calc_word_freq(data)

    plt.hist(freq.values(), bins=100)
    plt.show()

    # 頻度50以下の単語を除いてみる
    plt.hist(filter(lambda t: t>50, freq.values()), bins=100)
    plt.show()
    return 0


if __name__ == '__main__':
    main()
