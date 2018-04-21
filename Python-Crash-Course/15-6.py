# 15-6 自动生成标签

from random import randint

import pygal

class Die():
    """一个模拟骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为8面"""
        self.num_sides = num_sides

    def roll(self):
        """掷骰子"""
        return randint(1, self.num_sides)


die = Die()
results = [die.roll() for i in range(6000)]
values = [x for x in range(1, die.num_sides+1)]
frequencies = [results.count(x) for x in values]
print(frequencies)

# 绘图
hist = pygal.Bar()

hist.title = "掷六面骰子 6000 次的结果"
hist.x_labels = [str(value) for value in values]
hist.x_title = "结果"
hist.y_title = "结果的频率"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')
