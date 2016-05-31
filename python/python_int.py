#coding=utf-8
import pdb
class  int0(int):
	def __init__(self,value=0):
		if value < 0 :
			self = 0
		else : 
			self = value
	def __add__(self,y):
		if isinstance(y,int) :
			return int(self) + y
		else :
			raise ValueError()

if __name__ == "__main__":
	a = int0(-1)
	print a
	print a+1
	print a + "a"
