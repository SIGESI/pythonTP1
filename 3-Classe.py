from datetime import date
import time
import csv



class Date:

    day=0                            #两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs
    month=0
    year=0

    def __init__(self,day,month,year):      #两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
        self.day=day
        self.month=month
        self.year=year

    #surchage 重载 == 和 <
    def __eq__(self,other):

        return (self.year,self.month,self.day)==other
        #print()

    def __lt__(self, other):

        #age = Date.year - self.date.year - ((Date.month, Date.day) < (self.date.month, self.date.day))
        return  other<(self.month,self.day)
        #print()


class Etudiant:

    nom = ''
    prenom = ''
    date=Date

    def __init__(self,nom,prenom,date):
        self.nom=nom
        self.prenom=prenom
        self.date=date

    #fabrique l'adresse électronique prenom.nom@etu.univ-tours.fr
    def adresselec(self):
        monMail=self.prenom+'.'+self.nom+'@etu.univ-tours.fr'
        print(monMail)

    #Calculer l'âge de l'étudiant
    def age(self):
        #第一种方法 time
        #localtime = time.localtime(time.time())
        #age=localtime.tm_year - self.date.year - ((localtime.tm_mon, localtime.tm_mday) < (self.date.month, self.date.day))

        #第二种方法 date
        #today = date.today()
        #age=today.year - self.date.year - ((today.month, today.day) < (self.date.month, self.date.day))

        # 第三种方法 重载运算符 <
        localtime = time.localtime(time.time())
        date1 = Date(localtime.tm_mday, localtime.tm_mon, localtime.tm_year)
        age = date1.year - self.date.year - ( date1 < self.date )  #此处运算顺序存疑  对于date[0]，按一开始的顺序 结果有点不对。。。

        print(age)


                        #初始化用小括号直接开始
                        #date1=Date(29,9,1994)
                        #etu1=Etudiant("song","miyuan",date1)
                        #etu1.adresselec()
                        #etu1.age()

csvFile = open("fichetu1.csv", "r")
reader = csv.reader(csvFile)
listEtu=[]

for item in reader:
    time0=time.strptime(item[2],'%d/%m/%Y') #item[0]为当前迭代（当前行）的第一个元素
    date0=Date(time0.tm_mday,time0.tm_mon,time0.tm_year)
    etu=Etudiant(item[0],item[1],date0)
    listEtu.append(etu)  #list 追加

                        #test
                        #list[reader.line_num]=etu
                        #print(etu.adresselec())


listEtu[0].adresselec()
listEtu[0].age()

#连续赋值及比较实验，
#   1   1   =   1
#   0   1   =   0
#   1   0   =   1
#   0   0   =   0
#c=3-((11,28)<(10,20))
#print(c)