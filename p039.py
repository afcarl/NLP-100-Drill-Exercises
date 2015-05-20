#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""39. Zipfの法則

単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

from p030 import load_data
from p036 import calc_word_freq
import matplotlib.pyplot as plt


def main():    
    data = load_data()

    freq = calc_word_freq(data)
    freq = sorted(freq.values(), reverse=True)

    plt.loglog(range(1, len(freq)+1), freq)
    plt.show()

    return 0


if __name__ == '__main__':
    main()
