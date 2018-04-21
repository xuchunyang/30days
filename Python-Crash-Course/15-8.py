# 15-8 同时掷三个骰子

from random import randint
from collections import Counter
import pygal


values = [value for value in range(3, 19)]
results = [randint(1, 6) + randint(1, 6) + randint(1, 6)
           for i in range(10_0000)]
frequencies = [results.count(value) for value in values]

hist = pygal.Bar()

hist.title = '掷三个骰子 ' + str(10_0000) + ' 次'
hist.x_title = '和'
hist.y_title = '次数'
hist.x_labels = [str(value) for value in values]

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('d6-d6-d6.svg')

c = Counter([i+j+k
             for i in range(1, 7)
             for j in range(1, 7)
             for k in range(1, 7)])
print(c)

c_hist = pygal.Bar()
c_hist.x_labels = list(c.keys())
c_hist.add('D6 + D6 + D6', list(c.values()))
c_hist.render_to_file('3-d6.svg')
