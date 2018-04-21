# 15-7 两个八面骰子

from random import randint

import pygal


class Die():
    """模拟骰子"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die_1 = Die(8)
die_2 = Die(8)
values = [x for x in range(2, 17)]
times = 1000_0000
results = [die_1.roll()+die_2.roll() for i in range(times)]
frequencies = [results.count(value) for value in values]

hist = pygal.Bar()

hist.title = "掷两个八面骰子 " + str(times) + " 次的结果"
hist.x_labels = [str(value) for value in values]
hist.x_title = "结果"
hist.y_title = "结果的频率"

hist.add("D8 + D8", frequencies)
hist.render_to_file('dice_d8_d8_visual.svg')
