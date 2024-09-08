"""first=input('enter first number:')
operator=input('enter operator(+,-,*,/,%:')
second=input('enter second number:')

first=int(first)    ## both first and second are in string so first and second have conver in  integer
second=int(second)

if operator =='+':
    print(first+second)
elif operator =='+':
    print(first-second)
elif operator =='*':
    print(first*second)
elif operator =='/':
    print(first/second)
elif operator =='%':
    print(first%second)
else:
    print('invalid operator')"""

# #op=
# enter first number:2
# enter operator(+,-,*,/,%:*
# enter second number2
# 4


#op
# enter first number:5
# enter operator(+,-,*,/,%:/
# enter second number:2
# 2.5

###############################
"""
num1=int(input('enter your 1st nomber'))
num2=int(input ('enter your 2nd nomber'))
if num1>num2:
    print('num1 is greater')
else:print('num 2 is greater')
"""
#op=
# enter your 1st nomber5 ( presss enter)
#enter your 2nd nomber20 (press enter key) (else are executive)
#num 2 is greater








import sys

sys.exit()

l1=[1,2,3,10.5,True,False,None,True,False,'mumbai']
for i in l1:
    if type(i)==int:
        print(i)
#op=1,2,3







import sys
sys.exit()


l1=[1,2,3,10.5,True,False,None,True,False,'mumbai']
for i in l1:
    if type(i)==float:   #(out put only float pahije)
        print(i)
#op=10.5







import sys
sys.exit()
#print  only boolean nomber #(we can do  str, int, float)
l1=[1,2,3,10.5,True,False,None,True,False,'mumbai']
for i in l1:
    if type(i)==bool:
        print(i)
#op=True,False,true,False
import sys
sys.exit()



# print all o to 100 Odd number

for i in range(1,101,2):
    print(i)
#op=1,3,5,7.........95,97,99...
   

import sys
sys.exit()


# print all o to 100 even number

for i in range(0,101,2):
    print(i)
#op=0,2,4,6,8........96,98,100   (eaka khali eak print)





import sys
sys.exit()

for i in range(0,8,2):  #2 is step means skip 1 element
    print(i)
#op=  0
#     2
#     4
#     6

import sys
sys.exit()


for i in range(5,10,1):   #(start (5),end(10),,step(1) 1means skip o
    print(i)
#op=  5
#     6
#     7
#     8
#     9

import sys
sys.exit()


for i in range(5,10):
    print(i)
#op= 5
#    6
#    7
#    8
#    9



import sys
sys.exit()


import time
a='raj'
b=len(a)
for i in range(b):
    print(i)
    time.sleep(3)
#op=  0   (print index position of raj and one bone  iterated by  3 second)
#     1    (r=0,,a=1..j=2)
#     2


import sys
sys.exit()


import time
a='beed'
b=len(a)
for i in range(b):
    print(i)
#op= 0
#    1
#    2
#    3



import sys
sys.exit()

import time
a='mumbai'
for i in a:
    print(i)
    time.sleep(2) #(2 second aahet, you can change )
#op=  m   #(one by one iterate after 2 second)
#     u
#     m
#     b
#     a
#     i


import sys
sys.exit()

#in str one by one elemenr are iterated#
str='pune,govind'  #(str eavaji kahi pan uwse karu shkto.a,d.)
for i in str:
    print(i)

#op= p
#    u
#    n
#    e
#same asceh govind pn print hoil)
import sys
sys.exit()

a=1
if a%2==0:     ## this is the condition
    print('even')
else:
    print('odd')
#op=0dd

import sys
sys.exit()


a=2
if a%2==0:
    print('even')
else:
    print('odd')
#op=even

import sys
sys.exit()


x=5
if x>10:

    print('x is greater than 10')
else:
    print('x is not greater than 10')

#po=x is not greater than 10

#In this example, since the condition x > 10 is False (as x is assigned
#the value of 5), the code inside the else block will be executed. Therefore,
#the output will be;;;;;;:x is not greater than 10
import sys
sys.exit()
x=5
if x>10:

    print('x is greater than 10')
else:
    print('x is not greater than 10')
#op=x is not greater than 10



import sys
sys.exit()

##Identity operator##**
a=int(input('enter your number'))
if a%2==0:
    print('even')
else:
    print('odd')

import sys
sys.exit()

a=10
b=10
print('a' != 'b')#is not
#op=False


import sys
sys.exit()

a=10
b=10
print(a is b)
#op=True

import sys
sys.exit()

##Membership operator##
a='x'not in'hdyx'
print(a)
#op=False

import sys
sys.exit()
a='x'in 'hdyx'
print(a)
#op=True


import sys
sys.exit()

##*LOGICAL OPERATOR##
a=True
b=False
print(a or b)
#op=True

import sys
sys.exit()
a=True
b=False
print(a and b)
#0p=False

import sys
sys.exit()

##Relational operator##

a='Pune'## capital P
b='pune'## small p
print(a<b)
#op=True (use ascii code)

import sys
sys.exit()

a='d'
b='D'
print(a<b)
#op=False  (use ascii code (in ascii code capital letter value is always smaller than small letter value)
import sys
sys.exit()

a=100
b=500       #op#
print(a<b) #  True
print(a>b) #  False
print(a<=b) # True
print(a>=b) # False
print(a==b) # False
print(a!=b) # True



import sys
sys.exit()

a=True
b=5
print(a>b)
#op=False

import sys
sys.exit()


a=True
b=5
print(a<b)
#op=True



import sys
sys.exit()

## Arithmetick operator###

a=int(input('enter your 1st nomb '))
b=int(input('enter your 2nd nomb '))
print(a+b)
#op=25(at a run time take first nomber 10 and after that take second nomber is 15 then toatl=25)

import sys
sys.exit()

#**Pawar##**

a=10
b=2
print(a**b)
#op=100

import sys
sys.exit()

a=3
b=5
print(a**b)
#op=243





import sys
sys.exit()

#**Floor Division###

a=100
b=2
print(a//b)
#op=50


import sys
sys.exit()


a=100
b=50
print(a%b)
#op=0

#***Division##***


a=100
b=50
print(a/b)
#op=2.0


import sys
sys.exit()


##** Multipication##**
a=5.0
b=10.5
print(a*b)
#op=52.5



import sys
sys.exit


a='5'
b=10
print(a*b)
#op=5555555555  (string *integer  ka repeation aata hai)




import sys
sys.exit()


a=10
b=5
print(a*b)
#op=50

import sys
sys.exit()

#***** substraction###****

a='100'
b='200'
print(a-b)
#op=error( because in substraction string method is not suport (not use in )

import sys
sys.exit()

a=100
b=200
print (a-b)
#op==100


import sys
sys.exit()


a=False
b=True
print(a-b)
op=-1



import sys
sys.exit()

##**ddition###**

a=True
b=False
print(a+b)
#op=1

import sys
sys.exit()


a=True
b=True
print(a+b)

op=2




import sys
sys.exit()

#concatenation#

a='a'
b='b'
print(a+b)
#op=ab

import sys
sys.exit


#float+float=float
a=10.5
b=20.5
print(a+b)
#op=31.0

import sys
sys.exit()
a='100'
b='200'
print(a+b)
#op=100200



import sys
sys.exit()


a=100
b=200
print(a+b)
#op=300



import sys
sys.exit()

# int +int=int
var1=100
var2=200
print(var1+var2)
#o/p=300


import sys
sys.exit