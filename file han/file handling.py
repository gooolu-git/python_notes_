# # introduction to file handling
# # handling a file inside a python terminal id like accessing a file stored in a hard disk 
# # in file handling we bring the file stored in the hard disk to the ram or we can say in the pyhton shell

# reading and writing a file in a python 
# f=open('new.txt','w')
# f.write('gooluraja ')
# f.write('aman ')
# f.write('sanny')
# f.close()
# # we can do it here or we can do it into the pyhon shell too

# s=open('mytext.txt','w') #this is how we can create and write a file
# s.write('sumit singh')
# s.write('amit bhagel')
# s.close()


# m=open('mytext.txt','r')# this is how we  can read a file 
# n=m.read()
# print(n) 


# c=open('phone.txt','r')
# flag=0
# v='0'
# while(v!=''):
#     v=c.readline()
#     # if(v!=''):
#     n=int(v)
#     if(v==966902416):
#         print("number was matched")
#         flag=1
#         break
# if(flag==0):
#     print("number was not found")



# p=open('phone.txt','r')
# v='0'
# k=[]
# while(v !=""):
#     s=p.readline()
#     n=str(s)
#     k.append(n)
# print(k)

# f=open('test.txt','r')
# s=f.read(2)
# print(s)
# s=f.read(2)
# print(s)
# s=f.read(2)
# print(s)
# s=f.read(2)
# print(s)
# s=f.read(2)
# print(s)
# s=f.seek(7)# seek command can be used to navigate over the characters 
# s=f.read(2) # read 2 will read 2 characters , wheres read(1) will read 1 character 
# print(s)
# handling a genome seequece of a dataset
# g=open('genomeseq.txt','r')
# seq=g.read()
# print(seq)

# dia='AGTACC'
# print(dia in seq)
# covid='AGTACCC'
# print(covid in seq)


# handling a big file
# f=open('phone.txt','r')
# flag=0
# s='0'
# while(s!=''):
#     s=f.readline()
#     if(s!=''):
#         n=int(s)
#         if(n==9065235183):
#             print("the number was found")
#             flag=1
#             break
# if(flag==0):
#     print("the number was not found")


# handling a big file 
# import random
# f=open('phone.txt','r')
# for i in range(1000):
#     s=f.readline()
#     print(s)



# introduction to crytography
# caesar cipher
# import string
# d=[]
# s=string.ascii_lowercase
# d.append(s)

# # print(d)
# def diagonal_sum():
#     mat = []
#     diag = []
#     antidiag = []
#     d = int(input('enter the length of the matrix:'))
#     for i in range(d):
#         row =[]
#         for j in input().split(','):
#             row.append(int(j))
#         mat.append(row)
#     for i in range(len(mat)):
#         diag.append(mat[i][i])
#     for i in range(len(mat),0,-1):
#         antidiag.append(mat[i-1][i-1])
#     total = sum(diag) + sum(antidiag)
#     print(total)
# to find the num 0f times the substring appears in the original string 
# st = input('enter the original string:') # the original string
# subst = input('enter the substring:') # the substring
# n = len(subst)
# count = 0
# for i in range(0,len(st)):
#     if(st[i:i+n]==subst):
#         count += 1
# print(count)

# given a dictionary in which we have players as the 
# keys and a list containing the sports played by
# the player 
# def exact_two(players):
#     result = []
#     for man , value in players.items():
#         count = 0
#         for sports , play in value.items():
#             if play:
#                 count += 1
#         if count == 2:
#             result.append(man)
#     return result

# printing patterns 
# n = int(input('enter the rows'))
# for row in range(1,n+1):
#     for j in range(n-row):
#         print('.', end='')
#     for i in range(row,0,-1):
#         print(i,end='')
#     for k in range(2,row+1):
#         print(k,end='')
#     for i in range(n-row):
#         print('.',end='')
#     print()
# to remove the nt digit from a given string 
# def remove_digit(num,n):
#     numst = str(num)
#     m = len(numst)
#     output = ''
#     for i in range(-1 , - (m+1) , -1):
#         if abs(i) % n != 0:
#             output += numst[i] + output
#     return int(output)

# print(remove_digit(2646113,2))
# to change the of a string on given substring by  making the vowel to its next letter
# alpha = {'a':'b','e':'f','i':'j','o':'p','u':'v'}
# sen = input().split()
# sub = input()
# out = ''
# for word in sen:
#     if word == sub:
#         for j in range(len(sub)):
#             if(word[j] in alpha):
#                 out += alpha[word[j]]
#             else:
#                 out += word[j]
#         out += ' '
#     else:
#         out += word + ' '
# print(out.strip())
# function to divide the given string on n lines each lines have m characters
# def stripstring(word,l):
#     result = ''
#     for i in range(0,len(word),l):
#         result  += word[i: i + l] + '\n'
#     return result[:-1]
# print(stripstring('abcdefghijklmnopqrstuvwxyz',3))


# function to coumpute the combination in first line 
# and premutaion in second line 
# n = int(input())
# r = int(input())
# def factorial(n):
#     fact = 1
#     if(n==0):
#         return 1
#     return  n * factorial(n-1)

# def binomial(n,r):
#     if r == 0:
#         return 1
#     p = factorial(n)
#     c = factorial(r)
#     return p // (p-c) * c
# def permutaion(n,r):
#     if r == 0:
#         return 1
#     p = factorial(n)
#     c = factorial(r)
#     return p // (p-c)

# print(binomial(n,r))
# print(permutaion(n,r))

# function to perform the conctionation of two string if first last matches with the starting of the second string
# def joinwords(s,f):
#     for i in range(len(s)):
#         if(s[i:]==f[0:i+1]):
#             return (s+f[i:])
#         return (s+f)
# s = input()
# f = input()
# print(joinwords(s,f))
# def join_word(s,w):
#     for i in range(len(s)):
#         if(s[i:]==w[:i]):
#             return(s+w[i:])
#     return s+w
# s = 'sweden'
# w = 'denmark'
# print(join_word(s,w))


# fucntion to print the nuber into a string'
# def wordtonum(s):
#     numbers = {
#         'one':1,
#         'two':2,
#         'three':3,
#         'four':4,
#         'five':5,
#         'six':6,
#         'seven':7,
#         'eight':8,
#         'nine':9,
#         'zero':0
#     }
# s = input()
# t = input()
# def lettercount(s):
#     count = {}
#     for char in s:
#         count[char] = count.get(char,0) +1
#     return count
# s_count = lettercount(s)
# t_count = lettercount(t)
# for char in t_count:
#     if (char not in s_count) or (s_count != t_count[char]):
#         print(char)
#         break

# function to remove all the string from the second
# string from the first string 
# s1 = input()
# s2 = input()
# out = ''
# for i in s2:
#     if i in s1:
#         continue
#     out += i
# print(out)

# # function to print yes if the coin is distributable and no if the coin is not distributable
# x,y = map(int,input().spliit())
# total = x + 2*y
# if (x==0 and y %2 == 1) or (total % 2 == 1):
#     print('NO')
# else:
#     print('YES')


# function to sort a matrix coulumn 
# first create a function to get the coulum of the marix 
# then sort it and again apply that function again and make 
# the sorted column as the row of the matrrix
# n = int(input('enter the dim of matrix:'))
# m = []
# for i in range(n):
#     row = map(int,input().split(','))
#     m.append(row)


# function to convert the list to dict and dict to list

# def list_to_dict(l):
#     d = {}
#     for i in l:
#         d[i]=l[i]
#     return d
# def dict_to_list(d):
#     l =[]
#     for i in range(len(d)):
#         l.append(d[i]) # here the keys are 0,1,2,...so we can use the range function here correctly
#     return l

# funtio to print the sum of 1/2 + 3/4 + 5/6 + 7/8 ....
# n = int(input('enter a digit:'))
# series = 0
# for i in range(1,n+1):
#     num = 2*i -1 
#     den = 2*i
#     series += num /den
# print(round(series)) # the round builtin function returns the foat into nerest integer

# function to find the mean median and mode of a list l:
# def summary(l):
#     l.sort()
#     all = 0
#     n = len(l)
#     for i in l:
#         all += i
#     mean = all / n
#     maxi = 0
#     repeats = 0
#     mode_d = {}
#     for i in l:
#         mode_d[i] = mode_d.get(i,0) + 1
#     for k ,v  in mode_d.items():
#         if(mode_d[k] > maxi):
#             maxi ,  repeats = k,v
#     mode = maxi
#     median = 0
#     mid =  n//2 -1
#     if(n%2==1):
#         median = l[n//2]  
#     elif(n%2==0):
#         median = (l[n//2] + l[mid])//2
#     return mean , median ,mode

# p = [4,67,89,45,100,100]
# print(summary(p))


# # function to compute A**n where A is a squre matrix 
# # of size  n*n it returns A**n
# def mat_mul(p,q): # function to multiply matrix 
#     n = len(p)
#     m = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             val = 0
#             for k in range(n):
#                 val += p[i][k] *  q[k][j]
#             row.append(val)
#         m.append(row)
#     return m # m is a product of matirxes
# def power(a,n):
#     if(n==1):
#         return a
#     out = mat_mul(a,a)
#     for i in range(n-2):
#         out = mat_mul(a,out)
#     return out
# n = 4
# a = [[1,2,3],[4,5,6],[7,8,9]]
# print(power(a,4))


# given a file path we have to find the 
# extension name filenaem and depth of the 
# file:

path = "Users/GOOOLU/OneDrive/Desktop/python lecture/map.mp3"
l = path.split("/")
last = l[-1]
depth = len(l[1:-1])
filename , extention = last.split('.')
print(depth,filename,extention)

# we are given a dictionary for each trains
# where they stops
def get_stations(trains):
    # for each stations we have to find which train stops
    stations = {}
    for k , v in trains.items():
        for s in v:
            t=[]
            if(s not in stations):
                stations[s]=[]
            stations[s].append(k)
    return stations
trains = {'chennai express':['chennai','trichy','coimbatore'],
            'mumbai express':['mumbai','pune','nagpur','chennai'],
            'bengaluru express':['chennai','mumbai','bengaluru','mangalore','pune']
            }    

print(get_stations(trains))

def fraction(l):
    t = 0
    for i in l:
        t+=i[0]/i[1]
    return round(t)
def normalize(s):
    if(s.isupper()):
        return s.capitalize() + '!'
    else:
        return s.capitalize()
def valuecount(l):
    d = {
        '#':5,
        'o':3,
        'x':1,
        '!':-1,
        '!!':-3,
        '!!!':-5
    }
    total = 0
    for i in l:
        for char in i:
            total += d[char]
    if(total<0):
        return 0
    return total




# function to find the bonus amount 
# for a given period of time
def bonus(n):
    total = 0
    if(n<32):
        return 0
    elif(n<=40):
        return (n-32)*325
    elif(n<=48):
        return (n-40)*550+ 8*325
    else:
        return (n-48)*600 + 8*325 + 8*550

# given a list of string the string which
# occurs more than half the length of 
# list is the winner
def morevote(l):
    major = 0
    for vote in set(l):
        if(l.count(vote)>len(l)//2):
            return vote
    return None
# given a list of words if the specific word
# appears more than once we have to add
# s at their end else prnt the word
def plural(l):
    pl=set()
    for word in set(l):
        if(l.count(word)>=2):
            pl.add(word +'s')
        else:
            pl.add(word)
    return pl    

# def secret(s):
#     l = s.split('.')
#     final = 
#     first = l[0]
#     last = l[1:]


def prents(s):
    a = []
    b = ''
    for i in s:
        b += i
        if(b.count("(")==b.count(")")):
            a.append(b)
            b  = ''
    
