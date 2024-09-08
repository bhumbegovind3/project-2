


#import code  #### String####
#* string is colection of character/alphabet/object
# string have a single code ,double code,triple code.
#string is immutable (unchangable)
#string have index position .
#string work on positive and negative direction.
#string have unhashable in nature.
#string  work on different memory location..
#DUPLICATE value are allow






#confuse (error)
#print seprate character and seperate character#
s1='a4b1c2d'
s1=''
s2=''
for i in s1:
    if i.isalpha():
        s1=s1+i
else:
    s2=s2+i

import sys
sys.exit()
####################################################################
#print all the odd position character#
str='abcdefg'
print(str[1::2])
#op=bdf

##########################################################################
import sys
sys.exit()

#print all the even position character#
str='abcdefg'
print(str[0::2])
#op=aceg

############################################################
import sys
sys.exit()

#REVERSE THE STRING #

#reverse method 1#
str='pune'
print(str[::-1])
#op=enup

#########################################################
#reverse method 2#
str='pune'
s=''.join(reversed(str))
#op=enup

import sys
sys.exit()
############################################
#reverse method 3#(using list)
str='pune'
n=list(str)
n.reverse()
print(''.join(n))
#op=enup

###########################################################
#reverse method 4(own logick)#
str='pune'
result=''
for i in str:
    result=i+result
print(result)
#op=enup


###########################################################################3

import sys
sys.exit()
#confuse #
l1=['1''a''2''b']
s1='#'.join(l1)
print(s1)


######################################################################
l1=['1''a''2''b']
s1=''.join(l1)
print(s1)
#op=1a2b


######################################################
###SPLIT METHOD##

str='pune1mum1baiba1nglor1eche1nai'
l1=str.split('1')
print(l1)
#op=['pune', 'mum', 'baiba', 'nglor', 'eche', 'nai']

#######################################################


str='punem#umbai#banglorech#enai'
l1=str.split('#')
print(l1)
#op=['punem', 'umbai', 'banglorech', 'enai']

###########################################################


str='pune mumbai banglore chenai'
l1=str.split('e')
print(l1)
op=['pun', ' mumbai banglor', ' ch', 'nai']

#############################################################

str='pune mumbai banglore chenai'
l1=str.split()
print(l1)
#op=['pune', 'mumbai', 'banglore', 'chenai']


####################################################################

#addition only digit numer#Cconfuse #nahi aale
s1='pu1n3e589m'
s2=0
if s1.isdigit():
    s2=s2+int(s1)
    print(s2)


########################################################################

#print only digit#
str='pu1n3e589m'
for i in str:
    if i.isdigit():
        print(i)

############################################################################


#concate the string# (WRONG CONFUSE)

str1='bahubali 2 and krish 3 pathan'

for i in str1():
    if i.isdigit():
        print(i)


##########################################################

#in str print only number#
str='bahubali2 and krish 3 pathan'
for i in str:
    if i.isdigit():
     print(i)
#op= 2
#    3

#################################################


s='123govind'
print(s.isalnum()) #op-=True

##############################################

s='1 2 3 4 5 5'
print(s.isdigit()) #op=True  (only  all digit pahijet)

######################################################

s='PUNE'
print(s.isupper()) #op=True
print(s.islower()) #op=False

print(s.isalpha()) #op=True  (means all character are only small letter or capital pahije ...
                            #digit(nomber nahi pahije eak pan nahi tr error yete
                            #A to Z  and a to z pahije

##############################################################

s='ram'
print(s.islower()) #op=True  # (because all word are small)
print(s.isupper()) #op=False  #(because al word are small)

###########################################################################

s='sundar kanya '
print(s.endswith(' '))
#op=true  (kanya nanter space aahe so)



##########################################################

s='sundar kanya'
print(s.startswith('s'))  #op=True
print(s.startswith('sundar')) #op=True
print(s.startswith('Sundar')) #op=False (because S is capital)
print(s.startswith('sun'))  #op=True

print(s.endswith('a'))  #op=True
print(s.endswith('nya'))  #op=True






########################################################

s1='radha Is good,she is cute girl'
s2=s1.capitalize()
print(s2)
#op=Radha is good,she is cute girl


###################################################################

s1='radha is good .she is very cute girl'
s2=s1.title()
print(s2)
#op=Radha Is Good .She Is Very Cute Girl

################################################################

s1='ABCa bck ida jifa'
s2=s1.title()
print(s2)
#op=Abca Bck Ida Jifa

##########################################################################

s1='AbjdsahkA'
s2=s1.swapcase()
print(s1,s2)
#op=AbjdsahkA aBJDSAHKa ( convert lower to upper and upper to lower)


########################################################

s1='AbjdsahkA'
s2=s1.upper()
print(s2)
#op=ABJDSAHKA  (all small letter convert in to capital letter)

########################################################

s1='AbjdsahkA'
s2=s1.lower()
print(s2)
#op=abjdsahka (all capital letter convert into small letter)

####################################################

### COUNT AND REPLACE METHOD ###

s1='sundar kanya'
s2=s1.replace('kanya','balak')
print(s2)
#op=sundar balak

################################################################

s1='aaabcbsjdasjkAA'
s2=s1.replace('a','z')
print(s2)
#op=zzzbcbsjdzsjkAA  (only replce small a )


############################################

str='pune is big city'
print(str.count('t')) #op=1

#######################################################

str='abcdbavbbb'
print(str.count('b')) #op=5

################################################

#########################################

#### FIND, INDEX  METHOD ####

str='pune is city'

print(str.find('i'))  #op=5
print(str.find('is')) #op=5

print(str.rfind('t')) #op=10
print(str.rfind('i')) #op=9  (is and city made i ahe but right side print because r find)
print(str.rfind('p')) #op=0
print(str.find('city')) #op=8

print(str.index('i')) #op=5
print(str.index('is'))  #op=5

print(str.rindex('t')) #op=10
print(str.rindex('i')) #op=9
print(str.rindex('p')) #op=0
print(str.rindex('city')) #op=8


print(str.rindex('m')) #op= value errror   (because m is not present in str)

##############################################################################

s1=' pune '
print(id(s1)) #op=2558860350192
s2=s1.strip
print(id(s2))  #op=2558861791520  (before removing the spce and after removing the space  then the   memory address is different)

########################################


#Strip(lr)#####

a=' pune '
b=a.strip()
print(b)
#op=pune

#############################################

a=' pune '
b=a.rstrip()
print(b)
#op= pune (only right side space remove)

####################################################

a=' pune '
b=a.lstrip()
print(b)
#op=pune (only left side space remove)


######################################################


a=' pune '  #( in pune word before and after are single space )
print(len(a))
#op=6




###################################

a='pune'
print('u'in a)
#True
############################################

a='mam'
b=a[::-1]
if a==b:
    print('pallindrom')
else:
    print('not pallindrom')
#op=pallindrom


#########################################

a='beed'
b=a[::-1]
if a==b:
    print('pallindrom')
else:
    print('not pallindrom')

#op=not pallindrom

####################################################

#reverse the str##
a='govind'
print(a[::-1])
#op=dnivog

#################################################

#by using slicing method9start end step position)
t1=(1000,20,30,50,None,True,False,'str')

print(t1[::2])    #op=(1000, 30, None, False)

print(t1[1::2])  #(20, 50, True, 'str)

print(t1[2::2])  # (30, None, False)

print(t1[1:6:2])  #(20, 50, True)




##############################################

a='pune'
print(a[:])
#0p=pune

###########################################

a='pune'
print(a[0:2])
#op=pu

##########################################




#print the space position#

a=' mum bai '
for i in range(len(a)):
    if a[i]==' ':
        print(i)
#op= 0
#    4
#    8

###############################################

#print nomb of character in str#
a=' mum bai '
print(len(a))
#op= 9


####################################################

str='stepup'
for i in range(0,len(str)):
    if str[i] =='p':
        print(i)
#op=  3
#     5



##########################################


str='govind'
for i in range(0,len(str),2):   #(range(0,6,2) 2 means (-1) karyche means 1  skip hoil)
    print(i, str[i])
#op= 0 g
#    2 v
#    4 n

###########################################

#print character with index position)

str='raj'
for i in range(len(str)):
    print(i,str[i])
#op= 0 r
#    1 a
#    2 j

#########################################


str='raj'
for i in range(len(str)):
    print(str[i])
#op=  r
#     a
#     J

##############################################3

str='govind'
for i in range(len(str)):
    print(i)
#op=0,1,2,3,4,5 (s)


##################################################




