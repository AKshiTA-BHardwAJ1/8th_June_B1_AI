#############
#ASSIGNMENT 1
#############
#Q2.PERFORM FOLLOWING ON PYTHON SHELL
##>>> 5**9
##1953125
##>>> 3//2
##1
##>>> 7//3
##2
##>>> 6==6
##True
##>>> a=20
##>>> a+=30
##>>> a%=3
##>>> print(a)
##2
##>>> True*False
##0
##>>> True&False
##False
##>>> True and False
##False
##>>> ((6>3) and (7<4) or (18==3)) and (9>3)
##False
##>>> True is False
##False
##>>> False in 'False'
##Traceback (most recent call last):
##  File "<pyshell#13>", line 1, in <module>
##    False in 'False'
##TypeError: 'in <string>' requires string as left operand, not bool
##>>> ((True==False) or (False>True)) and (False <=True)
##False
 #################
#Q3.
s1="Nice to have it"
s2="here"
s1=s1+' '+s2
################
#Q4.
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
c=a[3][1][2]
###############
#Q5.
D=[s1,*a,s2]
###############
#Q6.
color_list_1=set(["white","black","red"])
color_list_2=set(["red","green"])

print(color_list_1.difference(color_list_2))
################
#Q7.
string=input("enter a string")
string.lower()
list=list(string)
set=set(list)
set.remove(' ')
t=len(set)
if t==26:
    print("string is pangram")
else:
    print("string is not pangram")
##################
#Q8.
s=input('enter a no')
t=eval('{0}+{0}{0}+{0}{0}{0}'.format(s))
print(t)
##################
#Q9.
S=input("enter some words: ")
t=S.split()
t.sort()
print('Sorted sequence of words are : ',t)
####################
#Q10.
d={'student':['Rahul','Kishore','Vidhya','Raakhi'],'marks':[57,87,67,79]}
m=(d['marks'])
print("Max marks are",(max(d['marks'])))
s=(d['student'])
print("Student who get max marks is",s[m.index(max(d['marks']))])

