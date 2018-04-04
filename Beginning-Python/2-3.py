#!/usr/bin/env python

sentence = input("输入一句话: ")

# +----------+
# |          |
# |  hello   |
# |          |
# +----------+
screen_width = 80
box_width = screen_width - 2
text_width = len(sentence)
left_marge = (box_width - text_width) // 2
right_merge = box_width - left_marge - text_width

print('+' + '-' * box_width  + '+')
print('|' + ' ' * box_width  + '|')
print('|' + ' ' * left_marge + sentence + ' ' * right_merge + '|')
print('|' + ' ' * box_width  + '|')
print('+' + '-' * box_width  + '+')
