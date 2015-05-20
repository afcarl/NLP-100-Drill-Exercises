#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""37. 頻度上位10語

出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

※日本語フォントの設定が必要
"""

from p030 import load_data
from p036 import calc_word_freq
import matplotlib.pyplot as plt


def main():    
    data = load_data()

    freq = calc_word_freq(data)
    # 上位10単語の取り出し
    words = sorted(freq.items(), key=lambda t:t[1], reverse=True)[:10]
    keys, values = zip(*words)  # キーと頻度に分ける

    width = 0.5
    plt.bar([i + width/2.0 for i in range(10)],
            values, width)
    plt.xticks([i + width for i in range(10)], keys)
    plt.show()
    return 0


if __name__ == '__main__':
    main()
