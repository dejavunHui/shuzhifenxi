import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False

'''
标准欧拉法
'''

class Mercy:

    def __init__(self):
        pass

    def __str__(self):
        return "代码作者:1607094148 卢辉"

    def __repr__(self):
        return self.__repr__()

    def euler(self, y, startx, endx, h):
        '''
        欧拉法
        :param y:
        :param startx:区间起点
        :param h:步长
        :return:
        '''
        xy = []
        xy_real = []
        n = len(y) - 1
        fx = np.poly1d(np.multiply(y[:n], range(n,0,-1)))
        y = np.poly1d(y)

        for i in range(startx,endx+1):
            fxy1 = fx(i)
            fxy2 = fx(i+h)
            fxy = 0.5*(fxy1+fxy2)
            if len(xy) == 0:
                yi = y(i)
                xy.append((i,yi))
                xy.append((i+h, yi+fxy*h))
                xy_real.append((i,y(i)))
                xy_real.append((i+h, y(i+h)))
            else:
                xy.append((i+h,xy[-1][1] + fxy*h))
                xy_real.append(((i+h, y(i+h))))

        self.rs = {}
        for (i,j) in xy:
            self.rs[i] = j

        self.real = {}
        for (i,j) in xy_real:
            self.real[i] = j

    def run(self, y, startx, endx, h):
        self.euler(y, startx, endx, h)
        self.plot()

    def plot(self):
        plt.figure(figsize=(8,4))
        plt.title("修恩法")
        plt.plot(list(self.rs.keys()), list(self.rs.values()),'b-')
        plt.plot(list(self.real.keys()), list(self.real.values()),'y-')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig('修恩法.png')
        plt.show()


if __name__ == '__main__':

    y = [-0.5, 4, -10, 8.5, 1]
    startx = 0
    endx = 10
    h = 0.5
    e = Mercy()
    e.run(y, startx, endx, h)