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

    def run(self, x):

        X = self.gauss(x)
        self.X_ = X
        print('上三角矩阵:')
        print(X)

        m, n = np.shape(X)
        self.rs = []
        for i in range(m-1, 0, -1):
            for j in range(n-2, 0, -1):
                if i == m-1:
                    try:
                        self.rs.append(X[i, -1]/X[i, i])
                    except ZeroDivisionError:
                        print('方程无解')
                    break
                temp = np.sum(np.multiply(self.rs, X[i, i+1:]))
                self.rs.insert(0, (X[i, -1]-temp)/X[i, i])
        print('解为:',self.rs)
        self.plot()

    def gauss(self, x):
        '''
        顺序高斯消去
        :param x: 矩阵元素
        :param m: 矩阵行数
        :param n: 矩阵列数
        :return:
        '''
        # X = np.matrix(np.array(x).reshape(m, n).astype(float))
        X = x
        m, n = np.shape(X)
        self.X = X.copy()
        print('原矩阵:')
        print(X)
        N = min(m, n)
        if m > n:
            X[n:m]=0

        for i in range(1, N):
            #增加主元的比较与交换
            for k in range(i, N):
                if abs(X[k, i-1])*1000 > abs(X[i-1, i-1])*1000:
                    X[i], X[k] = X[k], X[i]
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

    # x = [2, -1, 3, 1, 4, 2, 5, 4, 1, 2, 0, 7]
    # m = 3
    # n = 4
    # x = np.matrix(np.array(x).reshape(m, n).astype(float))
    g = GausseLimination()
    # g.run(x)
    # print(g)
    # print(g.X_)
    # print(g.X)

    x = np.array([
        [70, 1, 0, 636],
        [60, -1, -1, 518],
        [40, 0, 1, 307]
    ]).astype(float)
    x = np.matrix(x)
    g.run(x)
    print(g)