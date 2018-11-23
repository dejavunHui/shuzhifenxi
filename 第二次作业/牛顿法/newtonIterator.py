import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class NewtonIterator:

    def __init__(self,iters = None):
        '''

        :param iters:最大迭代次数
        '''
        self.iters = iters
        self.fig = None

    def initFig(self):
        self.fig = plt.figure(figsize=(8,4))

    def run(self,func,func_,x0,limitError = None,funcName = None):
        '''
        执行迭代
        :param func: 函数
        :param func_: 函数的一阶导数
        :param x0: 初值
        :param limitError:停止误差
        :param funcName:函数名称
        :return:
        '''
        self.initFig()
        i = 0
        x = x0
        xSet = [x]
        ySet = [func(x)]
        while True:
            i += 1
            x_b = x
            x = x - func(x)/func_(x)
            error = abs(x_b - x)
            xSet.append(x)
            ySet.append(0)
            xSet.append(x)
            ySet.append(func(x))
            if limitError and error < limitError:
                self.plot(func, xSet, ySet, funcName=funcName)
                break

            elif self.iters and i > self.iters:
                self.plot(func, xSet, ySet, funcName=funcName)
                break
            elif func(x) == 0:
                self.plot(func, xSet, ySet, funcName=funcName)
                break

    def plot(self,func,xSet,ySet,funcName):
        '''
                画图
                :param func:函数表达式
                :param xSet:迭代过程点x值
                :param ySet:迭代过程点y值
                :return:
                '''
        ax = plt.subplot(111)
        x = np.arange(min(xSet) - 1, max(xSet) + 1, 0.01)
        y = func(x)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('iterator')
        if funcName:
            plt.legend()
            plt.text(max(x) - .1, max(y) - .1, funcName)

        plt.plot(x, y, 'g-')
        plt.annotate(s='Approximate root of equation is %s' % (xSet[-1]), xy=(xSet[-1], ySet[-1]),
                     xytext=(xSet[-1] - 0.1, ySet[-1] + .1), arrowprops={'arrowstyle': '->'})
        ln, = ax.plot([], [], 'r-', animated=False)

        def init():
            ax.set_xlim(min(xSet) - 0.5, max(xSet) + 0.5)
            return ln,

        def gen():
            for i, j in zip(xSet, ySet):
                dot = [i, j]
                yield dot

        xdata = []
        ydata = []

        def updata(newdot):
            xdata.append(newdot[0])
            ydata.append(newdot[1])
            ln.set_data(xdata, ydata)
            return ln,

        ani = FuncAnimation(self.fig, updata, frames=gen, init_func=init, blit=True)
        ani.save('iterator.gif', writer='imagemagick', fps=1)

    def show(self):
        plt.show()

if __name__ == "__main__":

    f = lambda x: np.power(x, 4) + 3*x**2 - 4*x - 1
    f_= lambda x: 4 * x**3 + 6*x - 4
    it = NewtonIterator()
    it.run(func=f, func_=f_,x0=1.9, limitError=0.01)
    it.show()