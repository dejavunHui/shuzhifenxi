import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
弦截法实现双点弦
'''
class Secant:

    def __init__(self,iters = None):
        '''

        :param iters:最大迭代次数
        '''
        self.iters = iters
        self.fig = None

    def initFig(self):
        self.fig = plt.figure(figsize=(8,4))

    def run(self,f,x0,x1,limitError = None,point = 1,funcName = None):
        '''
        弦截法
        :param f: 函数
        :param x0:
        :param x1:
        :param point: 双点弦还是单点弦
        :param funcName: 函数名称
        :return:
        '''
        self.initFig()
        i = 0
        xb = x0
        xn = x1
        xSet = [x0,x1]
        ySet = [f(x0),f(x1)]
        while True:
            i += 1
            if point == 1:
                xb = xn
                xn = xn - f(xn)/(f(xn) - f(x0)) * (xn - x0)
            else:
                x = xn - f(xn)/(f(xn) - f(xb)) * (xn - xb)
                xb = xn
                xn = x

            error = abs(xn - xb)
            xSet.append(xn)
            ySet.append(0)
            xSet.append(xn)
            ySet.append(f(xn))
            if limitError and error < limitError:
                self.plot(f, xSet, ySet,point, funcName=funcName)
                break

            elif self.iters and i > self.iters:
                self.plot(f, xSet, ySet,point, funcName=funcName)
                break
            elif f(x) == 0:
                self.plot(f, xSet, ySet,point, funcName=funcName)
                break

    def plot(self,func,xSet,ySet,point,funcName = None):
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
            ax.legend()
            ax.text(max(x) - .1, max(y) - .1, funcName)

        plt.plot(x, y, 'g-')
        plt.annotate(s='Approximate root of equation is %s' % (xSet[-1]), xy=(xSet[-1], ySet[-1]),
                     xytext=(xSet[-1] + 0.1, ySet[-1] + .2), arrowprops={'arrowstyle': '->'})
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
        ani.save('iterator%s.gif'%point, writer='imagemagick', fps=1)

    def show(self):
        plt.show()

if __name__ == "__main__":

    f = lambda x: np.power(x, 3) + 3*x**2 + 4*x - 1
    it = Secant()
    it.run(f=f,x0=1.9,x1 = 1.5,point = 2, limitError=0.01)
    it.show()