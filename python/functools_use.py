#-*- coding: utf-8 -*-  

import pdb
  
def thisIsliving(fun):  
  def living(*args, **kw):  
    print living.__doc__
    return fun(*args, **kw) + u'活着就是吃嘛。'
    
  return living  
 
@thisIsliving  
def whatIsLiving():  
  u"什么是活着"  
  return u'对啊，怎样才算活着呢？'  
  
print whatIsLiving()  

print  
  
from functools import update_wrapper
def thisIsliving(fun):  
  def living(*args, **kw):  
    print living.__doc__
    return fun(*args, **kw) + u'活着就是吃嘛。'  
  return update_wrapper(living, fun)  
 
@thisIsliving  
def whatIsLiving():  
  u"什么是活着"  
  return u'对啊，怎样才算活着呢？'  
  
print whatIsLiving() 



from functools import wraps  
  
def thisIsliving(fun):  
  @wraps(fun)  
  def living(*args, **kw):  
    print living.__doc__
    return fun(*args, **kw) + u'活着就是吃嘛。'  
  return living  
 
@thisIsliving  
def whatIsLiving():  
  u"什么是活着"  
  return u'对啊，怎样才算活着呢？'  
  
print whatIsLiving()  