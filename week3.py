# # how to print first  n numbers in python
# for x in range(1,11):
#     print(x)

# # this will print the even number 
# eve=int(input("enter the number till you want to find the even numbers:"))
# for x in range(1 , eve+1):
#     if(x % 2 ==0 ):
#         print(x)
# # one line code        
# for x in range (2, eve+1 ,2):
#     print(x)
# # how to print in decreasing order
# for x in range(eve+1 , 2 ,2):
#     print(x)
# # how to print the first n  number in a single line separated by commas     
# n = 10
# # for x in range(1 , n+1):
# #     print(x,end=" ")

# # # how to print first 10 positive integers in a same line separated by commas     
# # y=10
# # for i in range(1,11):
# #     print(i , end = ",")
# # how to print each character of a string of a one on each line     
# word = "great"
# for char in word:
#     print(char)
# n=len(word)
# for i in range(n):
#     print(word[i])
# for c in word[0:-1]:
#     print(c,end=",")    
# print(word[-1])

# word = "malyalam"
# # enumerate
# for index , char in enumerate(word):
#     print(index,char)

# # enumerate is a perdefined function in pyton to aceess the index and the chaaracter of a string in an efficeint way 


# word = "easy"
# count= 0
# for char in word:
#     count += 1
# print(count)    


# word = "gooluraja"
# ch = "l"
# flag=False
# for char in word:
#     if ch == char:
#         flag=True
# if(flag == True):
#     print("FOUND")        
# else:
#     print('not found')    




# # word = "amanrajabetajiaapbaregyanihana"
# # ch = "a"
# # count = 0
# # for char in word:
# #     if ch == char:
# #         count += 1
# # print(count)        



# # num = int(input("enter a number:"))
# # while(num != 0):
# #     num = int(input("enter a number:"))

# # to find wheather a substing is present in string or not
# word = "shipping"
# ch = "i"
# index = 0
# prese = False
# while index < len(word):
#     char = word[index]
#     if(char == ch):
#         prese = True
#         break
#     index += 1
# print(prese)    

# # to print a particular pattern in a python using loops
# n =  5
# for x in range(1,n+1):
#     strin = "#" * x
#     print(strin)


# for x in range(1,5):
#     for y in range(x):
#         print('#',end="")
#     print()


# how to find the number of factors of a integer

# num = int(input("enter the the number you want to find the factors:"))
# count= 0
# for i in range(1,num+1):
#     if num % i ==0:
#         print(i , end=" ")
#         count += 1
# print(count)        

# to find wheater a number is a perfect or not
# num = int(input('ENTER A NUM TO FIND WHEATHER THE NUMBER IS PERFECT:'))
# adding = 0
# for x in range(1, num):
#     if num % x == 0:
#         adding += x
# if(adding == num):
#     print("PERFECT NUMBER")
# else:
#     print('NOT A PERFECT NUMBER')    



# to find the all the perfect number between 1 and 10000
# for n in range(1,10_001):
#     fsum = 0
#     for f in range(1,n):
#         if( n %f == 0):
#             fsum += f
#     if(fsum == n):
#         print(n)


# how to determine a number is a prime
# n= int(input("enter a number:"))
# count= 0
# for x in range(1 , n+1):
#     if(n % x ==0):
#         count += 1
# if(count == 2):
#     print('prime')
# else:
#     print("not prime")   

# another way to do it  
# n = int(input("enter a number:"))
# fired = True
# if (n==1):
#     print(False)
# else:    
#     for f in range(2,n):
#         if(n % f ==0):
#             fired = False
#             break
#     print(fired)


# how to find the pairs of positive integers who adds up to 100
# for x in range(1,100):
#     for y in range(1,100):
#         if(x+y ==100):
#             print(x,y)

# # anpther easy way to do this

# for x in range(1,100):
#     print(x,100-x)
# how to find the pythagorean triplert of the form (x,y,z) with x<y<z<100            


# for x in range(1,100):
#     for y in range(1,100):
#         for z in range(1,100):
#             if(x**2 + y**2 == z**2):
#                 if(x< y < z):
#                     print(x,y,z)

# Accept a string as input and print PALINDROME if it is a palindrome, and NOT PALINDROME otherwise.

# word = input()
# new=""
# h=len(word)
# for i in range(1,len(word)+1):
#     new += word[-i]
# if(new == word):
#     print('PALINDROME')   
# else:
#     print('NOT PALINDROME')



# Accept two strings as input and form a new string by removing all characters from the second string which are present in the first string.
# Print this new string as output. You can assume that all input strings will be in lower case.    
    
# word1  = input()
# word2  = input()
# new=""
# for char in word2:
#     if char not in word1:
#         new += char
# # new.replace(" ","")
# print(new)



# Two integers are co-prime if the only common divisor between the two integers is one.

# Accept two positive integers as input in two different lines. 
# Print Coprime if the two integers are co-prime, else print Not Coprime. Assume that both the integers are greater than two.


# marks = int(input())
# option = int(input())
# correctoptavail = input()
# answergiven = input()
# for char in answergiven:
#     if(char not in correctoptavail):
#         marks=0
#     else:
# accept two integer and print the sum of all the numbers that are divisible by a and b
# a=int(input())
# b=int(input())
# total = 0
# for i in range(1000,20010):
#     if(i%a == 0 ) and (i%b ==0):
#         total +=i
# print(total)  /

# to fiind wheather a  given pair is coprime or not

# n1 =int(input())
# n2=int(input())
# c= True
# for i in range(2,n1):
#     if(n1%i==0):
#         if(n2%2==0):
#             c=False
#             break
# if c :
#     print('coprime')
# else:
#     print("not coprime") 
# to find wheather a number is a string or a integer or a float value
# n=input()
# if  n[0]=="-":
#     n=n[1:] 
# c="0123456789."
# isstring = False
# for i in n:
#     if(i not in c):
#         isstring = True
       
# if not isstring:
#     if "." in n and n.count(".")==1  :
#         print('Float')      
#     elif(n.count(".")==0):
#         print('Integer')    
#     else:
#         print('None')
# else:
#     print("None")


# n=int(input())
# choices=int(input())
# correct = input()
# select = input()
# c=(len(correct)+1) //2
# m = 0.0
# for i in range(0,len(select),2):
#     if(select[i] in correct):
#         m += n/c
#     else:
#         m=0.0
#         break
#     print(m) 


# a = input()
# b = input()
# n1 = len(a)
# n2 =len(b)
# n = n1+n2
# w = ""
# while (n > 0):
#     if(len(a)==0):
#         w += b
#         break
#     elif(len(b)==0):
#        w += a
#        break
#     else:
#         if(a[0]==b[0]):
#             w += a[0]*2
#             a = a[1:]
#             b = b[1:]
#         elif(a[0]>b[0]):
#             w += b[0]
#             b = b[1:]
#             n -= 1
#         else:
#             w += a[0]
#             a=a[1:]
#             n -=1
# print(w)            


# num = int(input())
# totalsum = 0
# for i in range(1,num+1):
#     termsum =0
#     for j in range(1,i+1):
#         termsum += j
#     totalsum += termsum
# print(totalsum)        
# num =int(input())
# for i in range(2,num):
#     pri = num
#     if(num % i ==0):


# i = 1
# while(i <=10):
#     print("ram ram ")
#     i+=1
# to find the number of prime numbers in a given range
# n= int(input())
# total = 0
# for i in range (2 , n+1):
#     isprime = 1
#     for j in range(2,i):
#         if(i%j == 0):
#             isprime = 0
#             break
#     if(isprime):
#         total += 1
# print(total)           

# to find all the triplet in a given range

# n=int(input())
# num =0
# for i in range(1,n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if(i**2+ j**2 == k**2):
#                 print(i,j,k)
#                 num+=1
# if(num ==0):
#     print('NO SOLUTION')   

# to remove the character of one string to another string               
# string1 = input()
# string2 = input()
# temp = ""
# for i in range(len(string1)):
#     for j in range(len(string2)):
#         if(string2[i]==string1[i]):
#             continue
#         else:
#             temp += string2[j]
#     string2,temp = temp , ""
# print(string2)


# to check wheater a string is palindrome or not
# word = input()
# reverse = ""
# for char in word:
#     reverse = char + reverse  #here it is actually adding the character at the last of the new string instead of adding at the start of the string
# if(word == reverse):
#     print('PALINDROME')
    
# else:
#     print('NOT A PALINDROME')        

# print(reverse)


# or we can use the another cosde of indexing type
# word = input()
# new = ""
# l=len(word)
# for i in range(l-1,-1,-1):
#     new += word[i]
# if(new == word) :
#     print('PALINDROME') 
# else:
#     print('not a palindrome')    
# to check wheather two given numbers are coprimes or not
# num1 = int(input())
# num2 = int(input())
# num3 = max(num1,num2) here it is search for the maximum of the two numbers
# flag = 1
# for i in range(2,num3): here  we have to start with the 2 and before the 2nd last number from the last 
#     if(num1 % i == 0 and num2 % i ==0): here its checking wheater there is any factors of both of the numbers
#         flag = 0
#         break
# if(flag):
#     print('COPRIME')        
# else:
#     print('NOT COPRIMES')    

# to print the largest number from the sequence of numbers till we get the input as 0
# t = int(input())
# large = t
# while(t !=0):
#     if(t > large):
#         large = t
#     t = int(input())
# print(large) 

# this code will print  the  shortest string from a given sequence of inputs
# x = input()
# maxx= x
# m = len(x)
# while(x != 'abcdefghijklmnopqrstuvwxyz'):
#     if(len(x)< m):
#         m = len(x)
#         maxx = x
#     x = input()    
# print(maxx)    


# to print the sum of digits
# n = int(input())
# total = 0 #here we initialie our total to 0 
# while n > 0:
#     total += n%10  # here we are adding the remainder of a number after dividing with 10
#     n = n//10 # here we are removing the digit we have added already by the floor division
# print(total)


# to print the numbers smaller than the input number in a single line separated by commas
# n = int(input())
# for i in range(1,n+1):
#     if(i != n):     #here we are checking if the i is not equal to the n if it is equal then it will not execute and will end with comma before
#         print(i,end=",")
#     else:    # here if i == n then it will print n at the last without leaving a comma at the last
#         print(i)   

 