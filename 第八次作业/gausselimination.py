import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False
'''
顺序高斯消去
'''


class GausseLimination:

    def __init__(self):
        self.X = None
        self.X_ = None

    def __repr__(self):
        return '1607094148-卢辉'

    def run(self, x, m, n):
        X = self.gauss(x, m, n)
        self.X_ = X
        print('上三角矩阵:')
        print(X)
        self.plot()

    def gauss(self, x, m, n):
        '''
        顺序高斯消去
        :param x: 矩阵元素
        :param m: 矩阵行数
        :param n: 矩阵列数
        :return:
        '''
        X = np.matrix(np.array(x).reshape(m, n).astype(float))
        self.X = X.copy()
        print('原矩阵:')
        print(X)
        N = min(m, n)
        if m > n:
            X[n:m]=0

        for i in range(1, N):
            for j in range(i, N):
                try:
                    c = X[j, i-1]/X[i-1, i-1]
                    X[j] -= X[i-1]*c
                except:
                    raise ZeroDivisionError('除数为0,不能进行高斯消去')
        return X

    def plot(self):
        fig = plt.figure(figsize=(16, 8))
        c = ['yellow','blue']
        plt.subplot(121)
        m, n = np.shape(self.X)
        for i in range(m):
            for j in range(n):
                plt.scatter(i, j, c=c[np.abs(self.X[i, j])>0])
                plt.annotate(s='%s' % self.X[i, j], xy=(i, j), xytext=(i, j-0.1))
        plt.title('原矩阵')

        plt.subplot(122)
        plt.title('上三角矩阵')
        for i in range(m):
            for j in range(n):
                plt.scatter(i, j, c=c[np.abs(self.X_[i, j])>0])
                plt.annotate(s='%s' % self.X_[i, j], xy=(i, j), xytext=(i, j-0.1))
        plt.savefig('g.png')
        plt.show()


if __name__ == '__main__':

    x = [2, -1, 3, 1, 4, 2, 5, 4, 1, 2, 0, 7]
    m = 3
    n = 4
    g = GausseLimination()
    g.run(x, m, n)
    print(g.X_)
    print(g.X)