#coding=utf-8

"""
python 闭包
"""


def counter(start_at = 0):
	count = [start_at]
	def incr():
		count[0] += 1
		return count[0]
	return incr

if __name__ == "main" : 
	count = counter(5)

def method1():
	a = 1
	def method2():
		a +=1 
		print a 
	return method2

def method3():
	a = [1]
	def method2():
		a.append(a[0])
		print a 
	return method2

def method4():
	def method2(a=1):
		a += 1
		print a 
	return method2

def method5():
	a =  1
	def method2(a=a):
		a += 1
		print a 
	return method2

def method6():
	a =  {"count":1}
	def method2(a=a):
		a['count'] += 1
		print a['count']
	return method2

"""
import sys
sys.path.append("./")
from python_Closure import *
a = method5()
a()
"""