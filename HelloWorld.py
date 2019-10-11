print("Hello World")

a,b,c=1,1.2,"oh my dear"
print(a,b,c)
print(type(a),type(b),type(c))
print(isinstance(a,int))
print(type(isinstance(a,int)))
#Classe parent
class cl1:
    a1 = 11
    b1=21
#classe enfan
class cl2(cl1):
    a2=12

print("-------------jugez en classe-------------------")
c=(type(cl2())==cl1)
print("(type)cl2 = cl1 ? ", end="")
print(c)

c1=(isinstance(cl2(), cl1))
print("(isinstance)cl2 = cl1 ? ", end="")
print(c1)
print("-------------jugez en classe-------------------\n")


print("-------------Opération numérique-------------------")
print("2 // 4")
print(2 // 4)
print("2 / 4")
print(2 / 4)
print("2 ** 5")
print(2 ** 5)
print("-------------Opération numérique-------------------\n")

print("-------------String-------------------")
str="songmiyuan"
print(str)
print(str[0:-2])
print(str[3:6])
print(str[4:])
print(str *2)
print(str+" print")
print("-------------String-------------------\n")

#列表截取的语法格式如下： 变量[头下标:尾下标]
print("-------------List-------------------")
listTest = ["a","b","c","d","e","f"]
print(listTest[0:4])
print("-------------List-------------------\n")

#元组小括号()， 列表中括号[]
print("-------------Tuple-------------------")
tuble= ('first',21,2.333,21,121,32)
print(tuble[0:-2])
print("-------------Tuple-------------------\n")

'''
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
----------格式-----------------------------------
parame = {value01,value02,...}
或者
set(value)
'''
print("-------------Set-------------------")
#case 1
students={'tom1','tom2','tom3','tom1'}
print(students)
if 'song' in students:
    print("song is in students")
else :
    print("song is not in students")
#case 2
set1=set('songsdf')
set2=set('songeeeeeee')
print(set1)
print(set1-set2)
print(set1 | set2)
print(set1 & set2)
print(set1 ^ set2)
print("-------------Set-------------------\n")

#字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
print("-------------Dictionary-------------------")
#t1
dict={}
dict['one']="1-song"
dict[2]="2-song"
print(dict["one"])
print(dict[2])
#t2
dictLong={1:"firstValue",'two':"secondValue",'三':"中文三"}
print(dictLong.keys())
print(dictLong.values())
print("-------------Dictionary-------------------\n")

#! /usr/bin/env python3   ------这是加在文件里，让 .py 像shell一样执行

#为Logic创造的
def importHello(name):
    print('hello:',name,'，i come from helloworld.py')
    return
