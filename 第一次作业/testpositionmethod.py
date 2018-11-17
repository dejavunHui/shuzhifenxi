# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


class TestPositionMethod:

	def __init__(self,limit_dis=None,max_steps=None):
		'''
		params:
		limit_dis:区间长度终止条件
		max_steps:轮数终止条件
		'''
		if limit_dis is None and max_steps is None:
			raise Exception('至少有一个中断条件不为空')
		self.limit_dis = limit_dis
		self.max_steps = max_steps
		

	def __check__(self,fun,s,e):
		x = np.arange(s,e,0.1)
		y = fun(x)
		if np.sum(abs(y)-1e-6<0) == 0:
			raise Exception('请确保区间有根')

	def fit(self,fun,s,e,funname=None):
		'''
		params:
		fun:函数表达式
		'''
		self.__check__(fun, s, e)
		i = 0
		while True:
			if self.max_steps and i > self.max_steps:
				self.plot(fun,s,e,funname)
				break
			if self.limit_dis and abs(e - s) < self.limit_dis:
				self.plot(fun,s,e,funname)
				break
			m = (s*fun(e) - e*fun(s)) / (fun(e) - fun(s))
			if abs(fun(m)) - 1e-6 < 0:
				s = m
				e = m
				self.plot(fun,s,e,funname)
				break
			if fun(m) * fun(s) < 0:
				e = m
			else:
				s = m


	def plot(self,fun,s,e,funname=None):
		'''
		画图
		'''
		self.figure = plt.figure(figsize=(16,8))
		x = np.arange(s-5,e+5,0.1)
		y = fun(x)
		plt.plot(x,y,'r-')
		if funname:
			plt.legend()
			plt.text(max(x),max(y)-4,funname)
		plt.xlabel('X')
		plt.ylabel('Y')
		plt.xlim(s-6,e+6)
		plt.ylim(min(y),max(y))
		plt.title('dichotomy')
		plt.annotate(s='this is e: %s'%(e),xy=(e,0),xytext=(e+2,fun(e) - 1),arrowprops={'arrowstyle':'->'})
		plt.annotate(s='this is s: %s'%(s),xy=(s,0),xytext=(s-2,fun(s) - 1),arrowprops={'arrowstyle':'->'})
		plt.grid(True)
		plt.savefig('试位法结果图')
		plt.show()
		


if __name__ == '__main__':
	d = TestPositionMethod(limit_dis = 0.0001)
	f = lambda x:x**2 + 2*x - 3
	d.fit(f, -2, 2,'x^2 + 2x - 3')