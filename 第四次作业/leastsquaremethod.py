import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

'''
最小二乘法
'''


class LeastSquare:

    def __init__(self):
        pass

    def fit(self, x, y):
        '''
        寻找参数
        :param x:n*m数组,n为样本个数
        :param y: 标签值
        :return:
        '''
        n, m = np.shape(x)
        assert n == np.shape(y)[0]
        self.a0 = (n * np.sum(x*y,0) - np.sum(x,0)*np.sum(y))/(n*np.sum(x**2,0)-(np.sum(x,0))**2)
        self.a1 = (np.sum(x**2,0)*np.sum(y)-np.sum(x,0)*np.sum(x*y,0))/(n*np.sum(x**2,0)-np.sum(x,0)**2)

    def predict(self,x):
        return self.a1 * x + self.a0

    def plot(self,x,y):

        m,n = np.shape(x)
        if n == 1:

            fig = plt.figure(figsize=(8,4))
            plt.scatter(x,y,c='green')
            plt.plot(x,self.predict(x),'r-')
            plt.savefig('最小二乘.png')
            plt.show()



if __name__ == '__main__':
    L = LeastSquare()
    x = np.arange(10).reshape(10,1)
    y = np.array([1,3,2,4,5,7,6,8,9,10]).reshape(10,1)
    # x = np.random.randn(10,3)
    # y = np.random.randn(10,1)
    print(y)
    L.fit(x,y)
    print(L.predict(x))
    L.plot(x,y)
    print(L.a0,L.a1)