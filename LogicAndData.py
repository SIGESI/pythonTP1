import random
import sys
import HelloWorld
print("-------------逻辑运算符and or not-------------------")
a = 0
b = 0

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

print("-------------逻辑运算符and or not-------------------\n")

print("-------------成员运算符 in , not in -------------------")
a=10
list=[1,2,3,4,5,6,]

if(a in list):
    print("a is in list")
else:
    print("a is not in list")
print("-------------成员运算符 in , not in-------------------\n")

print("-------------随机数-------------------")
print(random.random())
a=random.uniform(20,30)
print(a)
b=round(random.uniform(5, 10), 2)
print('2位随机数是：',b)
print("-------------随机数-------------------\n")

print("-------------Python字符串格式化-------------------")
a="宋觅源"
b=24
print("我叫%s,今年%d岁"%(a,b))
print("-------------Python字符串格式化-------------------\n")

print("-------------三引号-------------------")
str="""
this is a sentence 
with 3 lines
!!!!!!!!!!!
"""
print(str)
print("--------------三引号------------------\n")

print("tuple:( ),list:[ ],dictionnaire:{ }\n")

print("--------------Fibonacci series------------------")
a,b=0,1
while b<10:
    print(b)
    a,b=b,a+b
print("--------------------------------")
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
print("end\n")
print("--------------Fibonacci series------------------\n")

print("-------------elif----------------")
'''
age=int(input("input your age:"))

if age<=0:
    print("are u kidding me ?")
elif age<18:
    print("oh child")
elif age>18:
    print("yes, u r big guy")
'''
print("-------------elif----------------\n")

print("-------------无限重复的啾啾--------------------")
#a=1
#while (a): print("啾啾：我喜欢源哥~~~~")
print("-------------无限重复的啾啾--------------------\n")

print("-------------iter--------------------")
list=[1,2,3,4,5]
it=iter(list)
'''
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''
print("-------------iter--------------------\n")

print("-------------函数--------------------")

def helloPrint(name):
    print("hello:",name)
    return

helloPrint("宋觅源")

print("-------------函数--------------------\n")

print("-------------模块--------------------")

#print('Python 路径为：', sys.path, '\n')

# 这是错误写法，还要加入.py 才能用
#   importHello('song')
HelloWorld.importHello('songHello')

print(sys.path)
print("-------------模块--------------------\n")
