import matplotlib.pyplot as plt

from random_walk import RandomWalk


rw = RandomWalk(50000)
rw.fill_walk()

# 设置绘制窗口的尺寸 英寸
plt.figure(figsize=(10, 6))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x, rw.y, c=point_numbers, cmap=plt.cm.Blues, s=1)

# 突出起点和终点
plt.scatter(0, 0, c='green', s=100)
plt.scatter(rw.x[-1], rw.y[-1], c='red', s=100)

# 隐藏坐标轴
ax = plt.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

plt.show()
