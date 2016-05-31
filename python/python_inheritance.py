#!/usr/bin/python
# -*- coding: UTF-8 -*-

class BaseClass(object):
   def __init__(self):
      print "调用BaseClass父类构造函数"

   def Method2(self):
      print "父类BaseClass的Method2"

class Parent(BaseClass):        # 定义父类
   parentAttr = 100
   def __init__(self):
      print "调用父类构造函数"

   def parentMethod(self):
      print '调用父类方法'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "父类属性 :", Parent.parentAttr

   def Method1(self):
      print "父类Parent的Method1"

class Parent1(BaseClass):
   parentAttr = 200
   def __init__(self,a) :
      print "调用父类Parent1构造方法"

   def parentMethod(self):
      print "调用父类parent1方法"

   def Method1(self):
      print "父类Parent1的Method1"


class Child(Parent,Parent1): # 定义子类
   def __init__(self):
      print "调用子类构造方法"

   def childMethod(self):
      print '调用子类方法 child method'

   def Method1(self):
      Parent.Method1(self)
      # super(Child,self).Method1()
      print "子类的Method1"

   def Method2(self):
      BaseClass.Method2(self)
      # super(Child,self).Method2()
      print "子类的Method2"

"""
#test
import sys
sys.path.append("./")
from python_inheritance  import *
a = Child()
a.Method1()
a.Method2()
"""