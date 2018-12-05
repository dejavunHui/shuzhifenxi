import numpy as np
import matplotlib.pyplot as plt


class NewtonInterPolation:

    def __init__(self):
        self.b = []

    def __str__(self):
        return '程序作者:1607094148-卢辉'

    def __repr__(self):
        return self.__str__()

    def clear(self):
        self.b.clear()

    def initB(self):
        for i in range(1, len(x)+1):
            # print(self.f(x[:i], fx[:i]))
            self.b.append(self.f(x[:i], fx[:i]))

    def run(self, xp, x, fx):
        # self.f(x, fx)
        if len(self.b) == 0:
            self.initB()

        rs = 0
        for i in range(len(self.b)):
            sub = 1
            for j in range(i):
                sub *= (xp - x[j])
            rs += sub * self.b[i]
        return rs

    def f(self, x, fx):
        assert type(x) == list
        assert type(fx) == list
        assert len(fx) == len(x)
        if len(x) == 1:
            return fx[0]
        rs = (self.f(x[:-1], fx[:-1]) - self.f(x[1:], fx[1:])) / (x[0] - x[-1])
        return rs

    def plot(self, xp, x, fx):
        fig = plt.figure(figsize=(8, 4))
        plt.title('newtoninterpolation')
        xs = np.arange(-5, 5, 0.1)
        ys = [self.run(xp=a, x=x, fx=fx) for a in xs]
        plt.plot(xs,ys,'r-')
        plt.scatter(x, fx, c='green')
        fxp = self.run(xp=xp, x=x, fx=fx)
        plt.scatter(xp, fxp, c='blue')
        plt.annotate(s='(%s,%s)'%(xp, fxp),xy=(xp, fxp),xytext=(xp+.5,fxp-.5))
        # for i,j in zip(x, fx):
        #     plt.annotate(s='(%s,%s)'%(i,j),xy=(i,j),xytext=(i-.2,j-.5))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig('newton%s'%int(xp))
        plt.show()


if __name__ == '__main__':
    n = NewtonInterPolation()
    print(n)
    x = [1, 3, 2]
    fx = [1, 2, -1]
    print('f(1.5)=%s' % n.run(xp=1.5, x=x, fx=fx))
    n.plot(1.5, x, fx)

    # plt.figure()
    print(n)
    n.clear()
    x2 = [0, 1, 2, 4]
    fx2 = [3, 6, 11, 51]
    print('f(0.5)=%s' % n.run(xp=0.5, x=x2, fx=fx2))
    n.plot(0.5, x2, fx2)