# class summary week 2 
# roll = int(input())
# Sapphire=[1,5,9,13,17,21]
# Peridot=[2,6,10,14,18,22]
# Ruby=[3,7,11,15,19,23]
# Emerald=[4,8,12,16,20,24]
# if(roll in Emerald):
#     print("Emerald")
# elif(roll in Sapphire):
#     print('Sapphire')
# elif(roll in Peridot):
#     print("Peridot")  
# elif(roll in Ruby):
#     print("Ruby")   



# first=int(input())
# second=int(input())
# third=int(input())
# fourth=int(input())
# ascending=[]
# ascending.append(first)
# ascending.append(second)
# ascending.append(third)
# ascending.append(fourth)
# ascending.sort()
# print(ascending[0],ascending[1],ascending[2],ascending[3])

# import datetime
# datein=input("%d-%m-%y")
# print(datein)





# weekly live session python week 2 



# num1=int(input("enter the first num:"))
# num2=int(input("enter  the second num:"))
# if(num1 > num2):
#     print(num1)
# else:
#     print(num2)    


#     # or

# num1=int(input("enter first num:"))
# num2=int(input("enter second num:"))
# print(max(num1,num2))



# checking for the word lenght 


# word=input("enter the word:")
# size=len(word)
# if(size <= 4):
#     print("short")
# elif (4<= size <= 8):
#     print("medium")    
# else:    
#     print("long")

# checking for positive and negative 

# new=float(input("enter the real num:"))
# if (-1<= new <0):
#     print("negative")
# elif(0< new <=1):
#     print("positive")    
# else:
#     print("")

# finding the  maximum between the numbers

# firstnum=float(input("enter the first num:"))
# secnum=float(input("enter the second number:"))
# thirdnum=float(input("entert the third number:"))
# print(max(firstnum,secnum,thirdnum))

# # problem6  checking for the trinagle or not  

# x=int(input("enter the first number"))
# y=int(input("enter the second number"))
# z=int(input("enter the third num"))
# if((x**2+y**2 == z**2)or 
#    (z**2 + y**2==x**2) or
#    (z**2 + x**2 ==y**2)): 
#     print("right")
# else:
#     print("not right")
# solving the same question with math library 
# # from math import sqrt

# from math import sqrt
# # print(sqrt(25))

# # ram
# # wrong code
# # here in function is used to seazrch avablity of sentence in list



# taking given group of words and a  sentence can be stiched or not


# word1,word2,word3=input('enter your first word:'), input('enter your second word:'),input('enter your third word:')
# sentence=input('enter your sentence:')
# space=""
# stich=False
# if(word1+space+word2+space+word3==sentence):
#     stich=True
# if(word1+space+word3+space+word2==sentence):
#     stich=True
# if(word2+space+word1+space+word3==sentence):
#     stich=True
# if(word2+space+word3+space+word1==sentence):
#     stich=True
# if(word3+space+word2+space+word1==sentence):
#     stich=True
# if(word3+space+word1+space+word2==sentence):
#     stich=True      
# if stich:
#     print("can't be stiched")    
# else:   
#     print("can be stiched ")



# problem7 pattern printing 

# for x in range(1,7):
#     print(x)
#  #here wenhave to gibve one more count more to print 
# for x in range(1 , 6):
#     print('#' * x )
#it willmprint hashes from 1 to 5
# "x "    is here a looop variable it will keeep increasing after one by one
# it will iterate over a range




# problem 9 printing all the even numbers in the given range
# for x in range(1,21):
#     if (x%2==0):
#         print(x)





# problem 10 finding the multiple of four or six in a given range 
# for x in range(1,101):        
#     if(x%4==0 or x%6==0):
#         print(x)



# problem 11  wrong code see below(checking for prime number)
# n=int(input("enter your number:"))
# if n == 0 or 1 or 2 or 3 or 5 or 7:
#     print("")
#     if(n%2 == 0 or n%3==0 or n%5==0 or n%7==0):
#         print("composite number")
#     else:    
#         print("prime")




# problem11 (checking for prime number)
# n=int(input("enter the number:"))
# count=0
# for f in range(2,n+1):
#     if n%f==0:
#         count=count+1
# if count==2:        
#     print("prime")
# else:    
#     print("not prime")

# import math as ma 
# print (ma.sqrt(25))


# finding prime in different way 


# n = int(input("enter a number:"))
# count = 0
# for num in range(2,n-1):
#     if(n%num==0):
#         count += 1
# if count == 0:
#     print("given number is prime")
# else:
#     print("given number is composite")   