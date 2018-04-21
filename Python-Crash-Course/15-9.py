# 15-9 将点数相乘

from collections import Counter
from random import randint
import pygal

def ideal():
    """理想结果"""
    results = [i*j for i in range(1, 7) for j in range(1, 7)]
    c_results = Counter(results)
    # FIXME 顺序有问题
    values = c_results.keys()
    frequencies = c_results.values()

    hist = pygal.Bar()
    hist.x_labels = values
    hist.add('D6 * D6', frequencies)
    hist.render_to_file('d6-multiply-d6-ideal.svg')

ideal()

def test():
    """实验结果"""
    times = 10_0000
    results = [randint(1, 6) * randint(1, 6) for i in range(times)]
    values = sorted(list(set([i*j for i in range(1, 7) for j in range(1, 7)])))
    frequencies = [results.count(value) for value in values]

    print(values)
    
    hist = pygal.Bar()
    hist.x_labels = values
    hist.add("D6 * D6", frequencies)
    hist.render_to_file('d6-multiply-d6-test.svg')

test()
