#!/usr/bin/env python
# coding: utf-8

# In[ ]:


m1= int(input("Enter marks for test1:"))
m2= int(input("Enter marks for test2:"))
m3= int(input("Enter marks for test3:"))
    
if m1<=m2 and m1<=m3:
     avgMarks=(m2+m3)/2
elif m2<=m1 and m2<=m3:
     avgMarks=(m1+m3)/2
elif m3<=m1 and m2<=m2:
     avgMarks =(m1+m2)/2
print("Average of best two test marks out of three test's marks is",avgMarks);


# In[ ]:


val = int(input("Enter a value:"))
str_val = str(val)
if str_val == str_val[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
for i in range(10):
    if str_val.count(str(i))>0:
        print(str(i),"appears",str_val.count(str(i)),"times");


# In[1]:


def fn(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn(n-1) + fn(n-2)
num = int(input("Enter a number : "))
if num > 0:
      print("fn(", num, ") = ",fn(num) , sep ="")
else:
      print("Error in input")


# In[3]:


def bin2Dec(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec += int(dig)*2**1
        i+=1
    return dec
def oct2Hex(val):
    rev = val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec +=int(dig)*8**i
        i+=1
    list=[]
    while dec!=0:
        list.append(dec%16)
        dec=dec//16
        n1+[]
        for elem in list[::-1]:
            if elem <=9:
                nl.append(str(elem))
            else:
                nl.append(chr(ord('A')+(elem-10)))
        hex="".join(n1)
        
        return hex
    
    num1=input("Enter a binary number:")
    print(bin2Dec(num1))
    num2=input("Enter a octal number:")
    print(oct2Hex(num2));
    


# In[ ]:


sentence = input("Enter a sentence:")

wordList = sentence.split("")
print("This sentence has",len(wordList),"words")

digCnt=upCnt=loCnt=0

for ch in sentence:
    if '0'<=ch <='9':
        digCnt+=1
    elif 'A'<=ch<='z':
        upCnt+=1
    elif 'a'<=ch<='z':
        loCnt+=1
        print("This sentence has",digCnt,"digits",upCnt,"uppercase letters",loCnt,"lower case letters")


# In[ ]:


str1 = input("Enter String 1\n")
str2 = input("Enter String 2\n")
if len(str2)<len(str1):
    short = len(str2)
    long=len(str1)
else:
    short = len(str1)
    long = len(str2)
matchCnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchCnt+=1
print("Similarity between two said strings:")
print(matchCnt/long)

