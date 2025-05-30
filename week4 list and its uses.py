# import random
# l=[]
# for i in range(30):
#     l.append (random.randint(1,365))
# l.sort()
# print(l)
# i=0
# flag=False
# while(i<len(l)-1):
#     if(l[i]==l[i+1]):
#         print( l[i],l[i+1],"is a repeatation")
#         flag=True
#         break
#     i=i+1
# if(flag==False):
#     print("there is no repeatation")    


# question:- print all the matching birthdays            

# import random
# l=[11,12,13,14,444]
# a=525554    
# for i in range(10000000):
#     l.append(random.randint(1,100000))
# flag=0 
# for j in range(l[i-1]):
#     if(a==l[i]):
#       print("hip hip hurreyeh match found") 
#       flag=1
#       break
# if flag==0:    
#     print("ohh no match not found") 
 
# naive search :- to search an element in a list of numbers

# import random
# l=[456565,252555,2025555,254555,256333,505023]
# a=505023   
# flag=0 
# for j in range(len(l)):
#     if (l[j] == a):
#         print("hip hip hurreh item matched")
#         flag=1
#         break

# if(flag==0):
#     print("ohh no match not found")  

 #the birthday paradox:-,here we have to find the maching birthdays
# import random
# l=[]
# flag=0
# for i in range(30):
#     l.append(random.randint(1,365))
# l.sort()
# print(l)
# i=0    
# while(len(l)>=0):
#     if(l[i]==l[i+1]):
#         print("hip hip hurreh match found",l[i],l[i+1]) 
#         flag=1
#         break
# #     i=i+1
# # if(flag==0):
# #         print("ohhh no match not found")    




# # now we will learn about sorting how it works            

# l=[1,23,23,465,89,3131,154,113,23656,6665]
# k=[]
# # min=l[0] 
# while(len(l)>0):
#     min=l[0] 
#     for i  in range(len(l)):
#         if(l[i]<min):
#             min=l[i]   
#     k.append(min)
#     l.remove(min) 
# print(k)

# # intro to dot product 

# # question to find the sum of all the numbers in a list
# # l=[1,2,3,4566,8899,98556]
# # sum=0
# # for i in range(len(l)):
# #         sum=sum+l[i]
# # print(sum) 


# # dot product
# # it is  actuallly a product and their sum
# # l=[1,2,2,3]
# # k=[5,6,5,8]
# # # dotproduct=(1*5)+(2*6)+(2*5)+(3*8)# we have to multiply and add the element at the same place
# # sum=0
# # for i in range(len(l)):
# #     sum=sum+(l[i]*k[i])
# # print(sum)    
    
# # matrix addition by first principle

# r1=[1,2,3]
# r2=[4,5,6]
# r3=[7,8,9]

# s1=[1,2,1]
# s2=[6,2,3]
# s3=[4,2,1]
# a=[]
# a.append(r1)
# a.append(r2)
# a.append(r3)

# b=[]
# b.append(s1)
# b.append(s2)
# b.append(s3)

# print(a)
# print(b)
# dim=3
# c=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(dim):
#     for j in range(dim):
#         c[i][j]=a[i][j]*b[i][j]
# print(c) #this is a dot product


# matrix multiplication :-cross product

# r1=[1,2,3]
# r2=[4,5,6]
# r3=[7,8,9]

# s1=[1,2,1]
# s2=[6,2,3]
# s3=[4,2,1]
# a=[]
# a.append(r1)
# a.append(r2)
# a.append(r3)

# b=[]
# b.append(s1)
# b.append(s2)
# b.append(s3)


# dim=3
# c=[[0,0,0],[0,0,0],[0,0,0]]

# for i in range(dim):
#     for j in range(dim):
#         for k in range(dim):
#             c[i][j]= c[i][j]+a[i][k]*b[k][j]
# print(c)  #this will return the cross product of these two matrix


# we can do all these things using numpy library function

# import numpy
# x=numpy.mat(a)
# y=numpy.mat(b)
# print(x*y)# boom we got it we have done it 

# this week 4 content has been ended now 












# weekly questions solutions 





# this week is about list and its uses
# word = 'PYTHON'

# x = 'y'
# print(word.find(x))
# here it will find the index position of the x if available otherwise it will return -1. find a string method 

# removing an element from a list 
# the pop method is used to remove a element from a list if we provide a index of the element and it will be removed
# l = [1,23,45,6,47,789,741,65555,55222,554525,55222,788,51225,552222,65222]
# print(l.pop()) #if we didnt specify the index of the element then it will remove the last element of the list
# print(l) #here the remaining list wil be printed

# remove method
# actaully it removes all the values matching to the arguumetnt
# l.remove(23) #it will remove all the values matching to 23
# print(l)

# reversing a list
# reverse = []
# lam =  len(l)-1
# for i in range(len(l)-1,-1,-1):
#     reverse.append(l[i])
# print(reverse)
# print(l.reverse())#this will do the same


# deleting all the contents of a list
# l.clear() # it will remove all the elements of list
# print(l)

# copying an list is useful when we wanna perform some operation on the list and dont want to change the original list
# x = l.copy() #here we have copied our oriinginal list into a duplicate list to make some operattions on it without disturbing the original list
# x[0]="mahavirba ke laika"
# print(x)
# print(l)

# how to print the element of a list multiple time
# a= 1
# for char in l :
#     a = a*char #it will find the product of all our element in the list and will store them in a variable called a
# print(a)    


# how to create a mtarix 
# actually a matrix is a list of list or lists whitin a list
# mat = []
# a=[1,2,3]
# b=[4,5,6]
# mat.append(a) # here also we are appending the list inside  a list
# mat.append(b) # here we are appending the list here also we are appending a list
# print(mat) # this will print the matrix


# how to take a list as a input and append it into a matrix and print the matrix at lastd
# dim = int(input('enter the dimension of the matrix you wanna create')) here we are accepting the dimension of the matrix by the user 
# mat = []
# for i in range(dim): here we are running the outer loop for the dim times
#     row = [] we initialised the row as list which will be appended thereafter here it is not a global variable it is a local variable which will be vanished after one iteration
#     for elem in input().split(','): here we are accepting the input from the user with comma separated values
#         row.append(int(elem)) here we are appending each element given into the input  into the row 
#     mat.append(row)   as we come out the loop we  append the readymade row into our matrix
# print(mat)    
 


# how to print the rows of a matrix in each line
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# n=len(mat[0])
# m=len(mat)
# for i in range(m):
#     for j in range(n):
#         if(j != n-1):
#             print(mat[i][j],end=",")
#         else:
#             print(mat[i][j])    
#     print()


# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# S = 0
# while len(L) >= 2:
#     S += L[0] + L[-1]
#     L = L[1:]
#     L = L[:-1]
# print(L)    


# Found = 0
# word = input().split(" ")
# matt = input()
# for elem  in word:
#     if (elem == matt):
#         found  = 1
# if (found == 0):
#     print('NO')        
# else:
#     print('YES')    

#  You are given a list marks that has the marks scored by a class of students in a Mathematics test. Find the median marks
#  and store it in a float variable named median. You can assume that marks is a list of float values.

# Procedure to find the median

# (1) Sort the marks in ascending order. Do not try to use built-in methods. Look at the lecture 4.5 of week-4 to get a better idea.

# (2) If the number of students is odd, then the median is the middle value in the sorted sequence. If the number of students is even, 
# then the median is the arithmetic mean of the two middle values in the sorted sequence.

# You do not have to accept input from the console as it has already been provided to you. You do not have to print the output to the console. 
# Input-Output is the responsibility of the autograder for this problem. Refer to PPA-11 if you are not sure how this works.      
# marks = [12,125,45,2.56,56.2,78,45,98]
# lamka = len(marks)
# new =[]
# while len(marks)>0:
#     mini = marks[0]
#     for i in range(len(marks)):
#         if(marks[i]<mini):
#             mini = marks[i]
#     new.append(mini)
#     marks.remove(mini)
# median = 0        
# if (lamka % 2 !=0):
#     mid = (lamka + 1)// 2
#     median = new[mid-1]
# else:
#     mid = lamka // 2
#     median = new[mid]+new[mid-1] / 2
# print(new)    
# print(median) 
# print(lamka) 



# n = int(input("enter the number of word to be entered:"))
# l = []
# for i in range(n):
#     word = input()
#     l.append(word)
# print(l)


# accept a sequence of comma separated integers as input and print the maximum 
# calulate the sequence as output
# l=[]
# for elem in input().split(","):
#     l.append(int(elem))
# print(max(l))    

# print the longest word in a list of words
# word = ["ram","aam","nahi","emli","khata","hai"] 
# maxi =word[0]
# for i in range(len(word)):
#     if(len(word[i])>len(maxi)):
#         maxi = word[i]
# print(maxi)   


# accept a space separeated sequence of positive real numbers as input . 
# convet each element of the sequence into the greatest integer less than
# or equal to it . print this sequence of integers as output with a comma 
# separated sequences of consecutive integers


# l = input().split(',')
# for i in range(len(l)):
#     l[i]=float(l[i])
#     l[i]=int(l[i])

# for j in range(len(l)):
#     if(j != len(l)-1):
#         print(l[j],end=',')
#     else:
#         print(l[j])    


# accept a sequence of comma separated words as input . reverse the sequence 
# and print it as output

# l = input().split(',')
# m = []
# for i in range(len(l)) :
#     m = [l[i]]+m
# print(m)



# accept a square matrix as input and store it in a variable name matrix .
# the first line of input will be n lines , where each line is a sequence
# of a comma separated integers that co n resposnds to one row of the matrix
# n = int(input())
# matrix = []
# for i in range(n):
#     row = []
#     for j in input().split(','):
#         row.append(int(j))
#     matrix.append(row)    
# print(matrix)


# accept a positive integer n as input and print the identity matrix of size
# n x n . your output should have n lines , where each line is a sequence of 
# n comma separated integers that corresponds to one row of the matrix
# n = int(input())
# mat = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         if i == j :
#             row.append(1)
#         else:
#             row.append(0)    
#     mat.append(row)
# for i in range(n):
#     for j in range(n):
#         if  j != n-1:
#             print(mat[i][j],end=',')
#         else:
#             print(mat[i][j]) 
              

# accept a square matrix A and an integer a as input and print the matrix A.
# as output . multiplying a matrix by an integer a is equivlent to multiplying 
# each element of the matrix by s . for example :
# n = int(input("enter the dimension of  the matrix:"))
# mat = []
# for i in range(n):
#     r = []
#     for j in input().split(' '):
#         r.append(int(j))
#     mat.append(r)
# s = int(input('enter the number by which you want to multiply with:'))
# for i in range(n):
#     for j in range(n):
#         mat[i][j]*=s
# for i in range(n):
#     for j in range(n):
#         if  j != n-1:
#             print(mat[i][j],end=' ')
#         else:
#             print(mat[i][j])     

# accept two square matrix A and B of dimension n x n as input and compute
# their sum  A + B 
# the first line will contain the integer n . this is followed by 2n lines 
# each line is a sequence if comma separated integers that denotes one row 
# of the matrix A . each of the last lines is a sequence of comma separated
# integers that denotes one row of the matrix B .
# your output agaiin be a sequence of n lines . where each line is a sequence
# of comma separated integers that denotes a row of the matrix A + B.

# n = int(input('enter the dimension of the matrix :'))
# a = []
# b = []
# total = []
# for i in range(n):
#     row = []
#     for j in input().split(','):
#         row.append(int(j))
#     a.append(row)
# for i in range(n):
#     row =[]
#     for j in input().split(','):
#         row.append(int(j))
#     b.append(row) 
# for i in range(n):
#     for j in range(n):
#         a[i][j] += b[i][j]
# for i in range(n):
#     for j in range(n):
#         if(i != n-1):
#             print(a[i][j],end=',')
#         else:
#             print(a[i][j])                     
#  maja aa gya  bro 

# l is a list of real numbers that is already given to you .
# you have to sort the list in decending order and store the sorted list
# in a vatriable called sorted_i .

# l = [45,56562,56331,413,55632,5632.23,23.2,56.45,0.231,2,56,89,5522,.235564]
# sorted_l= []
# while l !=[]:
#     mini = l[0]
#     for i in range(len(l)-1):
#         if(l[i]<mini):
#             mini = l[i]
#     sorted_l.append(mini)
#     l.remove(mini)
# print(sorted_l)  
          
# name = input().split(',')
# day =  input().split(',')
# newday = []
# for i in range(len(day)):
#     newday.append(int(day[i]))
# name.sort()
# newday.sort()
# common = []

# very very important question 
# names_input = input().split(',')
# birth_dates_input = input().split(',')

# birth_dates = []
# for date_str in birth_dates_input:
#     birth_dates.append(int(date_str))

# combined = []
# for i in range(len(names_input)):
#     combined.append((names_input[i], birth_dates[i]))

# for i in range(len(combined)):
#     for j in range(i + 1, len(combined)):
#         if combined[i][1] > combined[j][1]:
#             combined[i], combined[j] = combined[j], combined[i]

# common = []
# for i in range(len(combined)):
#     for j in range(i + 1, len(combined)):
#         if combined[i][1] == combined[j][1]:
#             if combined[i][0] < combined[j][0]:
#                 common.append([combined[i][0], combined[j][0]])
#             else:
#                 common.append([combined[j][0], combined[i][0]])

# print(common)



# n = int(input())
# all = []
# for i in range(n+1):
#     points = []
#     for j in input().split(','):
#         points.append(int(j))
#     all.append(points) 
# fixed = all[n-1]
# distace = []
# for i in range(n):
#     first = all[i]
#     distace.append(((fixed[0]-first[0])**2+(fixed[1]-first[1])**2)**0.5)
# combined = []
# for i in range(n-1):
#     combined.append(all[i],distace[i])
# bigger = combined[0][1]
# for i in range(len(combined)):
#     if(combined[i][1] > bigger):
#         bigger = combined[i][1]
# print(bigger)        

# number = 7  # Start with the smallest number in the sequence
# divisor = 2003  # The number we want to divide by

# while number % divisor != 0:
#     number = number * 10 + 7  # Add another 7 to the end of the number

# # Now, number contains the smallest number in the sequence that is divisible by 2003
# # Let's count the number of digits in number
# num_digits = len(str(number))

# print("The smallest number divisible by 2003 in the sequence has", num_digits, "digits.")


# L = [90, 47, 8, 18, 10, 7]
# S = [L[0]]	# list containing just one element
# for i in range(1, len(L)):
#     flag = True
#     for j in range(len(S)):
#         if L[i] < S[j]:
#             before_j = S[: j]	# elements in S before index j
#             new_j = [L[i]]		# list containing just one element
#             after_j = S[j: ]	# elements in S starting from index j
#             # what is the size of S now?
#             S = before_j + new_j + after_j
#             # what is the size of S now?
#             flag = False
#             break
#     if flag:
#         S.append(L[i])
# print(S)
                        




            


                    
