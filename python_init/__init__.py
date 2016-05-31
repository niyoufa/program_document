#coding=utf-8

class ManagementUtility(object):
	def  __init__(self):
		self.value = 0
	def __getitem__(self):
		return self.value
	def __setitem__(self,value):
		self.value = value