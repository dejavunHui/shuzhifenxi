import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False

'''
拉格朗日插值法
'''


class LargrangeInterpolation:

    def __init__(self):
        pass

    def __repr__(self):
        return '代码作者:1607094148-卢辉'

    def largange(self, xs, ys, x, n=None):

        '''
        拉格朗日插值多项式
        :param xs:已知点横坐标集合
        :param ys:已知点纵坐标集合
        :param x:插值点横坐标
        :param n:多项式项数,不指定则使用全部已知点
        :return:
        '''
        N = n if n else len(ys)
        rs = 0
        for i in range(N):
            fz = 1
            fm = 1
            for j in range(N):
                if j == i:
                    continue
                fz *= (x - xs[j])
                fm *= (xs[i] - xs[j])
            rs += (fz/fm)*ys[i]
        return rs

    def plot(self, xs, ys, x, n=None):
        fig = plt.figure(figsize=(8,4))
        y = self.largange(xs=xs, ys=ys, x=x, n=n)
        plt.title('拉格朗日插值法')
        plt.scatter(xs, ys, c='blue')
        plt.scatter(x, y, c='red')
        plt.annotate(s='(%s, %s)' % (x, y),xy=(x, y),xytext=(x, y-20), arrowprops={'arrowstyle':'->'})
        a = np.arange(-5, 5, 0.1)
        b = [self.largange(xs=xs, ys=ys, x=i, n=n) for i  in a]
        plt.plot(a, b, 'y-')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig('largange%s' % int(x))
        plt.show()

if __name__ == '__main__':
    l = LargrangeInterpolation()
    print(l)
    xs = [1, 3, 2]
    ys = [1, 2, -1]
    x = 1.5
    y = l.largange(xs=xs, ys=ys, x=x)
    print('f(1.5)=%s' % y)
    l.plot(xs=xs, ys=ys, x=x)

    print(l)
    xs = [0, 1, 2, 4]
    ys = [3, 6, 11, 51]
    x = 0.5
    y = l.largange(xs=xs, ys=ys, x=x)
    print('f(0.5)=%s' % y)
    l.plot(xs=xs, ys=ys, x=x)
