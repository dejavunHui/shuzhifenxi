import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False

class LU:

    def __init__(self):
        self.L = None
        self.U = None
        self.B = None

    def __str__(self):

        return "代码作者:卢辉-1607094148"

    def __repr__(self):
        return self.__str__()

    def LU(self, x):
        m, n = np.shape(x)
        N = min(m, n)
        # if m > n:
            # x[n:m] = 0
        self.L = np.matrix(np.zeros((N, N)))
        self.L[N-1,N-1] = 1
        for i in range(1, N):
            #增加主元的比较与交换
            self.L[i-1, i-1] = 1
            # for k in range(i, N):
            #     if abs(x[k, i-1])*1000 > abs(x[i-1, i-1])*1000:
            #         x[i], x[k] = x[k], x[i]
            for j in range(i, N):
                try:
                    c = x[j, i-1]/x[i-1, i-1]
                    self.L[j,i-1] = c
                    x[j,:-1] -= x[i-1,:-1]*c
                except:
                    raise ZeroDivisionError('除数为0,不能进行高斯消去')
        self.U = x[:,:-1]
        self.B = x[:,-1]

    def run(self, x):
        self.LU(x)
        print(self.L)
        print(self.U)
        print(self.B)
        D = self.L.I * self.B
        print(D)
        X = self.U.I*D
        print('解为%s'%X)
        self.plot()

    def plot(self):

        fig = plt.figure(figsize=(16, 8))
        c = ['yellow','blue']
        plt.subplot(121)
        m, n = np.shape(self.L)
        for i in range(m):
            for j in range(n):
                plt.scatter(i, j, c=c[np.abs(self.L[i, j])>0])
                plt.annotate(s='%s' % self.L[i, j], xy=(i, j), xytext=(i, j-0.1))
        plt.title('L矩阵')

        plt.subplot(122)
        plt.title('U矩阵')
        m, n = np.shape(self.U)
        for i in range(m):
            for j in range(n):
                plt.scatter(i, j, c=c[np.abs(self.U[i, j])>0])
                plt.annotate(s='%s' % self.U[i, j], xy=(i, j), xytext=(i, j-0.1))
        plt.savefig('LU.png')
        plt.show()


if __name__ == '__main__':

    # x = np.array([
    #     [70, 1, 0, 636],
    #     [60, -1, -1, 518],
    #     [40, 0, 1, 307]
    # ]).astype(float)
    x = np.array([
        [2, 2, 3, 3],
        [4, 7, 7, 1],
        [-2, 4, 5, -7]
    ]).astype(float)
    x = np.matrix(x)
    lu = LU()
    lu.run(x)
