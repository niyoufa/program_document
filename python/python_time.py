#coding=utf-8
import datetime
import threading
import sys  , pdb
# from tkinter import *  
pdb.set_trace()
minute = 60 * int(sys.argv[1])  
Curtime = datetime.datetime.now()  
print ("时间为：",Curtime)  
Scrtime = Curtime + datetime.timedelta(0,0,minute)  
print("目标时间：",Scrtime)  

def wait():  
	threading._sleep(minute)  

def Stat():  
	pdb.set_trace()
	Dsttime = datetime.datetime.now()  
	tmp = Dsttime - Scrtime + Scrtime  
	print("当前时间：",tmp)  
	if tmp == Dsttime:  
		print "时间到了" 
	else:  
		print("NO")  
wait()  
Stat() 