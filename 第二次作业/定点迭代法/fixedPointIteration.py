import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as an

class Iterator:
    '''
    开放法之迭代法
    '''

    def __init__(self,iters = None):
        '''

        :param iters: 最大迭代次数
        '''

        self.iters = iters
        self.fig = None
    def __check__(self,x0,func):
        '''
        检验方程是否可以使用迭代法
        :param func:
        :param x0:
        :return:
        '''
        x = np.arange(x0-1,x0 + 1,0.01)
        y = func(x)
        rs = y - x

        if min(abs(rs)) > 1e-2:
            raise Exception('方程不能使用迭代法')

    def initFig(self):

        self.fig = plt.figure(figsize=(8,4))


    def run(self,func,x0,limitError = None,funcName = None):
        '''
        执行迭代
        :param func:函数
        :param x0:初始值
        :param limitError:停止误差
        :return:
        '''
        self.__check__(x0,func)
        self.initFig()
        i = 0
        x = x0
        xSet = [x]
        ySet = [func(x)]
        while True:
            i += 1
            x_b = x
            x = func(x)
            error = x_b - x
            xSet.append(ySet[-1])
            ySet.append(ySet[-1])
            xSet.append(xSet[-1])
            ySet.append(func(xSet[-1]))
            if limitError and error < limitError:
                self.plot(func,xSet,ySet,funcName = funcName)
                break

            elif self.iters and i > self.iters:
                self.plot(func, xSet, ySet,funcName = funcName)
                break

    def plot(self,func,xSet,ySet,funcName = None):
        '''
        画图
        :param func:函数表达式
        :param xSet:迭代过程点集合
        :param ySet:
        :return:
        '''
        ax = plt.subplot(111)
        x = np.arange(min(xSet) - 1,max(xSet) + 1,0.01)
        y = func(x)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('iterator')
        if funcName:
            plt.legend()
            plt.text(max(x)-.1,max(y)-.1,funcName)

        plt.plot(x,y,'g-')
        plt.annotate(s='Approximate root of equation is %s'%(xSet[-1]),xy=(xSet[-1],ySet[-1]) ,xytext=(xSet[-1] - 0.1,ySet[-1] + .1),arrowprops={'arrowstyle':'->'})
        ln, = ax.plot([],[],'r-',animated=False)

        def init():
            ax.set_xlim(min(xSet) - 0.5,max(xSet) + 0.5)
            return ln,

        def gen():
            for i,j in zip(xSet,ySet):
                dot = [i,j]
                yield dot

        xdata = []
        ydata = []

        def updata(newdot):
            xdata.append(newdot[0])
            ydata.append(newdot[1])
            ln.set_data(xdata,ydata)
            return ln,
        ani = an.FuncAnimation(self.fig,updata,frames=gen,init_func=init,blit=True)
        ani.save('iterator.gif',writer='imagemagick',fps=1)

    def showFunc(self,func,funcName=None):
        '''
        展示原本函数图像
        :param func:原函数
        :return:
        '''
        x = np.arange(-5, 5, 0.1)
        y = func(x)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('function')
        l = plt.plot(x, y, 'g-')
        if funcName:
            plt.legend()
            plt.text(max(x) - .1,max(y) - .1,funcName)


    def show(self):
        plt.show()

if __name__ == '__main__':

    f = lambda x:np.power(x+1,1/3)
    f_o = lambda x:np.power(x,3) - x - 1
    it = Iterator()
    it.run(func=f,x0=1.5,limitError=0.01)
    it.show()
