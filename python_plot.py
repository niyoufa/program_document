import string
import matplotlib.pyplot as plt  
import numpy as np

def get(n) : 
	for i in range(n) : 
		yield i 

def y(x_list) : 
	for i in x_list : 
		yield i ** 2

def print_plot(x) : 
	plt.plot( list( get(x) ) , list( y( list( get(x) ) ) ) ) 
	plt.show()

print_plot(100)