import pdb	

class people(object) :
	def __init__(self,name,age):
		self.name = name
		self.__age = age
	def getName(self):
		return self.name
	def getAge(self):
		return self.__age
class man(people):
	def __init__(self,name,age):
		pdb.set_trace()
		super(man,self).__init__(name,age)

"""
super(man,self)
<super: <class 'man'>, <man object>>

"""