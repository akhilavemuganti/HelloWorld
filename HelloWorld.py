# print("Hello World")
#
# n1=4;n2=6;n3=9
#
# s1="Akhila";s2="Vemuganti";s3="Python"
#
# print(n1,n2,n3)
#
# print(s1," ",s2)
#
# print(s3[2:5])
#---------------------------------------------------
# LISTS

list1=["Apples","bannanas","strawberries"]

print(list1)

print(list1[2])

list2=list1.append("cherries")

print(list1)

del list1[1]

print(list1)

#---------------------------------------------------

#DICTIONARIES
# Key Value Pairs

students={"Akhila":32,"Laxmi":33,"Harish":29}
print(students)

print(students["Laxmi"])
print(len(students))

#Dictionary Functions

#students.del() #Deelete the entire dictionary
len(students)
print(students.keys())
print(students.values())
students.clear() # Empties all the values in he dict

#---------------------------------------------------

#TUPLES
#Cant be modified
#Same as lists but cant be modified

tup1=("Apple",67,"Ball")
print(tup1)
#---------------------------------------------------

#Conditional Statements
n=9
if(n>10):
    print("n is greater than 10")
else:
    print("n is less than 10")

n=9
if(n>10):
    print("n is greater than %d " %n)
elif():
    print("n is less than %d" %n)
else:
    print("n is %d" %n)


# and or conditions
#if(2>1 and 3<7)

 #if(2>1 0r 5>4)

#---------------------------------------------------

#For Loop

list1=["Apples","Bannana","Cherries"]
tup1=(6,7,8,9)

for i in list1:
    print(i)

for j in tup1:
    print(j)

for i in range(1,11):
    print(i)

for j in range(0,11,2):
    print(j)


for i in range(5,105,5):
    print(i)

#---------------------------------------------------

#While loop

c=0
while(c<5):
    print(c)
    c=c+1


#break, continue,pass(filler code to write functionality later)


"""
#Comments
"""

try:

except:


# ---------------------------------------------------
#Functions:

def add(num1,num2):
    sum1=num1 + num2
    print("Sum of %d" %num1 +" and %d" %num2+ " is %d" %sum1)

add(5,20)

#---------------------------------------------------

#In built Functions:

dir()

help()
#---------------------------------------------------

#Classes and objects

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getname(self):
            print("Name is "+self.name)
    def getage(self):
            print("Age is "+self.age)

p=Person("ABC","20")
p.getname()
p.getage()

#---------------------------------------------------

#Files

testFile=open("FileName")
testFile.read()
testFile.tell() #Specifies cursor position
testFile.seek() #Move the cursor at desired position by using offset
testFile.close()';;//'
