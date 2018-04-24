from random import choice


class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有的随机漫步都始于 (0, 0)
        self.x = [0]
        self.y = [0] 

    def get_step(self):
        """生成一个随机步数"""
        direction = choice((1, -1))
        distance = choice((0, 1, 2, 3, 4))
        step = direction * distance
        return step
        
    def fill_walk(self):
        """生成随机漫步的所有点"""

        while len(self.x) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标
            x = self.x[-1] + x_step
            y = self.y[-1] + y_step
            
            self.x.append(x)
            self.y.append(y)
