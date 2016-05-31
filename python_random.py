如果你对在Python生成随机数与random模块中最常用的几个函数的关系与不懂之处，下面的文章就是对Python生成随机数与random模块中最常用的几个函数的关系，希望你会有所收获，以下就是这篇文章的介绍。
random.random()用于生成
用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成随机数
?
1
n: a <= n <= b。如果 a <b， 则 b <= n <= a。
?
1
2
3
4
5
6
print random.uniform(10, 20)  
print random.uniform(20, 10)  
#---- 
#18.7356606526  
#12.5798298022  
random.randint
用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，Python生成随机数
?
1
2
3
print random.randint(12, 20) #生成的随机数n: 12 <= n <= 20 
print random.randint(20, 20) #结果永远是20 
#print random.randint(20, 10) #该语句是错误的。 
下限必须小于上限。
random.randrange
从指定范围内，按指定基数递增的集合中 ，这篇文章就是对python生成随机数的应用程序的部分介绍。
随机整数：
>>> import random
>>> random.randint(0,99)
21
随机选取0到100间的偶数：
>>> import random
>>> random.randrange(0, 101, 2)
42
随机浮点数：
>>> import random
>>> random.random() 
0.85415370477785668
>>> random.uniform(1, 10)
5.4221167969800881
随机字符：
>>> import random
>>> random.choice('abcdefg&#%^*f')
'd'
多个字符中选取特定数量的字符：
>>> import random
random.sample('abcdefghij',3) 
['a', 'd', 'b']
多个字符中选取特定数量的字符组成新字符串：
>>> import random
>>> import string
>>> string.join(random.sample(['a','b','c','d','e','f','g','h','i','j'], 3)).r
eplace(" ","")
'fih'
随机选取字符串：
>>> import random
>>> random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] )
'lemon'
洗牌：
>>> import random
>>> items = [1, 2, 3, 4, 5, 6]
>>> random.shuffle(items)
>>> items
[3, 2, 5, 6, 4, 1]