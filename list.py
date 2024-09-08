##   code will be chaange ######

# NESTED LIST#

l1=[10,20,[10,'pune'],['mumbai,100']]

print(l1[3]) #op= ['mumbai,100']
print(l1[-1]) #op=['mumbai,100']
print(l1[2][0]) #op=10
print(l1[2][1]) #op=pune

#print(l1[2][2])#op=index error  (2nd index position is not present)

print(len(l1)) #op=4
n

import sys
sys.exit()

l1=[2,3,4,5,1]
l1.sort()
#op=[1, 2, 3, 4, 5]
##

# (decending order use)
l1.sort(reverse=True)
print(l1)
#op=[5,4,3,2,1]

##

#(ascending order use)
l1.sort(reverse=False)
print(l1)
#op=[1, 2, 3, 4, 5]


import sys
sys.exit()

import sys
sys.exit()


import sys
sys.exit()

l1=[10,20,30,40,50]
l1.pop(2)
print(l1)
#op=[10, 20, 40, 50] (pop on index base)


import sys
sys.exit()

l1=[10,20,30,]
l1.pop()
print(l1)
#op=[10, 20] (nomal pop means last position pop)
import sys
sys.exit()

l1=[10,20,30,]
num=50
l1.extend(num)
print(l1)
#op=type error  (50 is only string this is not iterable so error)
# (50 he  list made pahije[50]
import sys
sys.exit()


list1=[]   #  (given empty list 1)
str1='pune'
list1.extend(str1)
print(list1)
#op=['p', 'u', 'n', 'e']

import sys
sys.exit()

list1=[] #  (given empty list 1)
str1='pune'
list1.append(str1)
print(list1)
#op=['pune']

import sys
sys.exit()

#EXTEND#
l1=[10,20,30,None,False,True]
l2=[10,20]
l1.extend(l2)
print(l1)
#op=[10, 20, 30, None, False, True, 10, 20]


import sys
sys.exit()

l1=[10,20,30,None,False,True]
l2=[10,20]
l1.append(l2)
print(l1)
#op=[10, 20, 30, None, False, True, [10, 20]]

print(l1)
import sys
sys.exit()

#APPEND #
l1=[10,20,30,None,False,True]
l1.append('muma')
#op=[10, 20, 30, None, False, True, 'muma']

print(l1)
import sys
sys.exit

l1=[10,20,30,None,False,True]
l1.remove(20)
print(l1)
#op= [10, 30, None, False, True]

import sys
sys.exit()

l1=[10,20,30,None,False,True]
l1.insert(2,'pune')
print(l1)
#op=[10, 20, 'pune', 30, None, False, True]
##

l1.insert(-1,'pune')
print(l1)
#op=[10, 20, 30, None, False, 'pune', True]


import sys
sys.exit()

l1=[1,10,20,30]
l1.insert(1,100)
print(l1)
#op=[1, 100, 10, 20, 30] (1  index position var 100 insert karyche)

import sys
sys.exit()
#print the two nomber sum =10#
l1=[1,9,-1,11,10,2,20,3,30,5,6,4,5,0]
n=len(l1)
for i in range(n):
 for j in range(i+1,n):
    if l1 [i]+l1[j]==10:
        print(l1[i],l1[j])
#op=
# 1 9
#1 11
#10 0
#5 5
#6 4


import sys
sys.exit()

#sort this list without using any inbuild function#
l1=[1,4,6,7,8,3,3,2]
l1.sort()
print(l1)
#op=[1, 2, 3, 4, 6, 7, 8] (sort means serial made print zale paHIJE)

import sys
sys.exit()

#print only integer value in list
l1=[1,2,3,4,5.5,True,False]
for i in l1:
    if type(i)==int:
        print(i)
#op s= 1,2,3,4  (you can print float  and bool value)
import sys
sys.exit()

l1=[1,2,3,4,5,3,7]
print(l1.index(3)) #op=2

print(3 in l1) #op=True
print(3 not in l1) #op= False


import sys
sys.exit()

# ADDITION OF LIST#
l1=[10,20]
l2=[30,40]
print(l1+l2)
#op=[10, 20, 30, 40]




import sys
sys.exit()

#multipcation of list#
l1 = [10, 20, 30]
n = 3
print(l1 * n)
# op=[10, 20, 30, 10, 20, 30, 10, 20, 30]

# own logick
print(l1 * 3)
# op=[10, 20, 30, 10, 20, 30, 10, 20, 30]


import sys

sys.exit()

# COUNT/MAX/MIN##
l1 = [1, 2, 2, 3, 2, 4, 10, 9]
print(l1.count(2))  # op=3

print(max(l1))  # op=10
print(min(l1))  # op=1

print(sum(l1))  # op= 33

import sys

sys.exit()

# print only odd number#
l1 = [10, 11, 12, 30, 31]
for i in l1:
    if i % 2 == 1:
        print(i)
# op=11
#   31
import sys

sys.exit()
# print only even number#
l1 = [10, 11, 12, 30, 31]
for i in l1:
    if i % 2 == 0:
        print(i)
# op s= 10,12,30


import sys

sys.exit()

l1 = [1, 1, 2, 3.3, 'pune', 'True']
for i in l1:
    print(i)
# ops=
# 1
# 2
# 3.3
# pune
# True

# print index position
for i in range(len(l1)):
    print(i)
# op=
# 0
# 1
# 2
# 3
# 4
# 5

##print charactern and its index position#
for i in range(len(l1)):
    print(i, l1[i])
# 0p=
#  0 1
# 1 1
# 2 2
# 3 3.3
# 4 pune
# 5 True

# print only even index position

for i in range(len(l1)):
    if i % 2 == 0:
        print(l1[i])
# op s=  2 pune


import sys

sys.exit()

l1 = [1, 1, 2, 3.4, 'pune,True,False']
# print(id(l1)) #op1251179648448 (before change id)
l1[0] = 'mumbai'
print(l1)  # op=#op=['mumbai', 1, 2, 3.4, 'pune,True,False']
# print(id(l1)) #op=1251179648448  (after change id)
# (id of list is same befor the change and after the change )


import sys

sys.exit()

l1 = [1, 1, 2, 3.4, 'pune,True,False']
print(len(l1))  # op=5
##
print(l1[::3])  # op=[1, 3.4]
print(l1[::-1])  # op=['pune,True,False', 3.4, 2, 1, 1]
print(l1[3::1])  # op=[3.4, 'pune,True,False']
print(l1[100])  # op= index error(100 index position is not present)
