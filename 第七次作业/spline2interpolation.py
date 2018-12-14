import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] =False

class Spline2Interpolation:

    def __init__(self):
        self.S = None#分段插值函数的系数表

    def run(self, xs, ys, x):
        S = self.fit(xs, ys)
        self.S = S.reshape(-1,3)
        n = len(xs)
        for i in range(1,n):
            if xs[i] >= x:
                k = i-1
                break

        y = np.multiply(self.S[k],[x**2, x, 1]).sum().astype(float)

        print('f(%s) = %g'%(x, y))
        s.plot(xs, ys, x, y)

    def fit(self, xs, ys):
        assert len(xs) ==  len(ys)
        n = len(xs) - 1
        X = np.matrix(np.zeros((3*n, 3*n)))
        for i in range(n):
            X[i, i*3:i*3+3] = [xs[i]**2, xs[i], 1]

        X[i+1, i*3:i*3+3] = [xs[i+1]**2, xs[i+1], 1]
        for i in range(n - 1):
            X[i+n+1,i*3:i*3+3]=[xs[i+1]**2, xs[i+1], 1]

        for i in range(n - 1):
            X[i+2*n, i*3:i*3+6] = [2*xs[i+1], 1, 0, -2*xs[i+1], -1, 0]

        X[-1,0] = 1
        Y = ys + ys[1:-1] + [0]*n
        Y = np.array(Y).reshape(-1, 1)
        Y = np.matrix(Y)
        return X.I * Y

    def plot(self, xs, ys, x, y):

        def getK(x):
            for i in range(1, len(xs)):
                if xs[i] >= x:
                    return i - 1

        fig = plt.figure(figsize=(8, 4))
        plt.title("二次样条插值")
        plt.xlabel('X')
        plt.ylabel('Y')
        for i, j in zip(xs, ys):
            plt.scatter(i ,j, c='blue')

        plt.scatter(x, y, c='red')
        plt.annotate(s='(%s, %s)'%(x,y),xy=(x,y),xytext=(x+.3,y+.3),arrowprops={'arrowstyle':'->'})

        # a = np.arange(-1*max(xs), max(xs), 0.1)
        # b = [np.multiply(self.S[getK(i)], [i**2, i, 1]).sum() for i in a]
        c = ['r-','g-','y-','o-','b-']
        for i in range(len(xs) - 1):
            a = np.arange(xs[i], xs[i+1],0.1)
            b = [np.multiply(self.S[getK(k)], [k**2, k, 1]).sum() for k in a]
            plt.plot(a, b,c[i % 5])
        plt.savefig('spline2.png')
        plt.show()

if __name__ == '__main__':

    s = Spline2Interpolation()
    xs = [3, 4.5, 7, 9]
    ys = [2.5, 1, 2.5, 0.5]
    # xs = [1, 2, 3]
    # ys = [1, 4, 9]
    s.run(xs, ys, 8)
