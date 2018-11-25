import numpy as np
import matplotlib.pyplot as plt

'''
贝尔斯托法求多项式根
'''

class Bairstow:

    def __init__(self,iters = None):
        '''

        :param iters:最大迭代次数
        :param x:多项式的根
        '''
        self.iters = iters
        self.x = []
        self.detUs = []
        self.detVs = []

    def getBN(self,a,u,v):
        '''
        求bn
        :param a:多项式系数
        :param u:因子式一次项系数
        :param v:因子式常数项
        :return:
        '''
        b = []
        b.append(a[0])
        b.append(a[1] - u * b[-1])
        n = len(a) - 1
        i = 2
        while i <= n:
            b.append(a[i] - u * b[-1] - v * b[-2])
            i += 1
        return b

    def getCN(self,b,u,v):
        '''
        求cn
        :param b: 商式系数
        :param u: 因子式一次项系数
        :param v: 因子式常数项
        :return:
        '''
        c = []
        c.append(b[0])
        c.append(b[1] - u * c[-1])
        i = 2
        n = len(b) - 1
        while i <= n - 2:
            c.append(b[i] - u * b[-1] - v * b[-2])
            i += 1
        return c

    def run(self,fl,u0,v0,e):
        '''
        贝尔斯托法求多项式根
        :param fl:多项式系数,list,[a0,a1,a2,...]
        :param u0:因子式一次项系数
        :param v0:因子式常数项
        :param e:终止误差
        :return:
        '''

        if len(fl) < 2:
            print('请输入正确的多项式系数')
            return -1
        if len(fl) < 3:
            self.x.append(np.roots(fl))
            print('x = ',np.roots(fl))
            return 1
        if len(fl) < 4:
            x = np.roots(fl)
            if len(x) == 1:
                X = [x[0], x[0]]
            else:
                X = x
            self.x.append(X)
            print('x = ', X)
            return 1

        detU = []
        detV = []
        i = 0
        while True:
            i += 1
            b = self.getBN(fl, u0, v0)
            c = self.getCN(b, u0, v0)
            r0 = b[-2]
            r1 = b[-1] + u0 * r0
            s0 = c[-2]
            s1 = c[-1] + u0 * s0
            '''
            r0 + c1 * detU + c2 * detV = 0
            r1 + c3 * detU + c4 * detV = 0
            '''
            c1 = u0 * s0 - s1
            c2 = -s0
            c3 = v0 * s0
            c4 = -s1
            detU.append((c2 * r1 - c4 * r0)/(c1 * c4 - c2 * c3))
            detV.append((c1 * r1 - c3 * r0)/(c2 * c3 - c1 * c4))
            u0 += detU[-1]
            v0 += detV[-1]

            if abs(detU[-1]) < e and abs(detV[-1]) < e:
                # x1 = .5 * (-u0 + np.sqrt(u0 ** 2 - 4 * v0))
                # x2 = .5 * (-u0 - np.sqrt(u0 ** 2 - 4 * v0))
                self.detUs.append(detU)
                self.detVs.append(detV)
                x = np.roots([1, u0, v0])
                print("x = ",x)
                self.x.append(x)
                break

            if i > self.iters:
                print('迭代失败,可以尝试增大迭代次数')
                break
        self.run(b[:-2],u0,v0,e)

    def plot(self,fl):

        x = np.arange(-2, 3, 0.01)
        y = np.arange(-2, 3, 0.01)
        n = len(fl)
        fl = fl[::-1]
        zreal = 0
        zcomp = 0
        for i in range(n):
            zreal += fl[i] * x ** i
            zcomp += fl[i] * y ** i
        fig = plt.figure(figsize=(16, 8))
        axr = fig.add_subplot(122)
        axr.plot(x,zreal,'r-')
        axr.plot(x,np.zeros(x.shape),'g-')
        j = 1
        try:
            for dot in self.x:
                for i in dot:
                    plt.scatter([i.real], [0],edgecolors='green')
                    plt.annotate('%.5g'%i.real,xy=(i,0),xytext=(i,j * 0.4),textcoords='offset points',
                            ha='center',va='top')
                    j = -j
        except:
            pass
        axr.set_title('real')

        axl = fig.add_subplot(121)
        for u,v in zip(self.detUs,self.detVs):
            axl.plot(u,v,'o--')
        axl.set_title('detU - detV')

        plt.savefig('bairstow')
        plt.show()



if __name__ == '__main__':

    b = Bairstow(1000)
    f = [1,-1.8,0.15,0.65]
    f = [1,-3.5,2.75,2.125,-3.875,1.25]
    u = -1
    v = -1
    b.run(f,u,v,0.01)
    b.plot(f)
    # print('2 next')
    # b.run(f2,u,v,0.01)