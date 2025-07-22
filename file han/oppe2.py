# given two list we have to swap the 
# elem of the list and find the product
# of the max of both the liist
def swap(a,b):
    for i in range(len(a)):
        if(a[i]>b[i]):
            a[i],b[i]=b[i],a[i]
    return max(a)*max(b)



# assume we have a string and a scrolling 
# bord of width n we have to print the 
# scrolling the text 
# def scroll(word,w):

# given n people in a circle every person 
# kills the person to its left we have to
# find the survivor
# def survivor(n):
#     l = list(range(1,n+1))
#     while(len(l)>1):
#         l = l[2:]+[l[0]]
#     return l
# print(survivor(41))

# function to find the value of a list 
# of given cards with combination
# def cardvalue(l):
#     acec =[]

#     d = {
#         2:10,
#         3:10,
#         4:10,
#         5:10,
#         6:18,
#         7:21,
#         'A':16,
#         'J':10,
#         'Q':10,
#         'K':10
#     }
#     acecount = []
#     for i in l:
#         if(i[1]=='A'):
#             acecount.append()


# starting with either 3 or 5 and return 
# true or false we can add 5 or multiply by 3
# we have to keep doing this until 
# # we reach the target number n 
# def reach(n):
#     if(n == 5) or (n== 3) :
#         return True
#     if(n<3):
#         return False
#     return reach(n/3) or reach(n-5)
# print(reach(14))

# given a list of string and a mask word
# we have to return a list of work which 
# matches the mask pattern
# def check(w,m):
#     if(len(w)!=len(m)):
#         return False
#     for i in range(len(w)):
#         if(m[i]!='*' and m[i]!=w[i]):
#             return False
#     return True
# def s(w,m):
#     return sorted([word for word in w if check(word,m)])

# print(s(['red','dee','cede','reed','decree','creed'],'*ree**'))

# accepting a list of integers and returning'
# the count of primes if they are at prime position
def prime(n):
    if(n<1):
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
    return True
def prime_glory(l):
    count = 0
    for i in range(2,len(l)):
        if(prime(l[i])) and prime(i):
            conunt += 1
    return count


# we have given a and b , a is the number of lin/es
# and first and last lines have b stars in it 
# and all the others lines have two stars at the start and end of the edges
# a=int(input('enter the number of lines'))
# b = int(input('enter the number of o:'))
# for i in range(a):  # this will go for a lines
#     if(i==0 or i == a-1):
#         print('o'*b)
#     else:
#         print('o'+' '*(b-2)+'o')
    


# we are given a 2d metal plate whose x and y 
# coordintes are not more than 5 ie 0to 5
# we are given a mathematical function to find the 
# temperature for given coordinate if the given 
# temperature is less than the calculated temperature
# then return true else flase: 
def survival(t):
    for x in range(0,6):
        for y in range(0,6):
            tem = 30 + (x**2) + (y**2) -(3*x) -(4*y)
            if(tem  <= t):
                return True
    return False
# given a l as list of integers we have to find the
#standard deviation of the list
def stadard_dev(l):
    mean = sum(l)/len(l) # here we found the mean of the list
    st = []
    for i in l:
        v = (i-mean)**2
        st.append(v) # here we append all the deviation in st
    return sum(st)/(len(l)-1) # here we return the deviation


# we are given a list of parentesi
#we have to determine that is it balanced or not
# balance that the order of opening and closing
#brackets should be equal and in right order
def balanced(word):
    stack = []
    opening = "({["
    closing= ")}]"
    parenmap =  {')': '(', '}': '{', ']': '['}
    for char in word:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack: # it means stack is empty or len(stack == 0)
                return False
            last = stack.pop()
            if parenmap[char] != last:
                return False
    return not stack
print(balanced('([{}])'))

# def balanced(word):
#     stack = []
#     opening = "({["
#     closing = ")}]"
#     paren_map = {')': '(', '}': '{', ']': '['}
    
#     for char in word:
#         if char in opening:
#             stack.append(char)
#         elif char in closing:
#             if not stack:
#                 return False
#             last_open = stack.pop()
#             if paren_map[char] != last_open:
#                 return False
    
#     return len(stack) == 0




# function to check wheater a group of brackets are balanced or not 
def balanced(l):
    open = '({['
    close = ')}]'
    parent = {'}':"{",')':"(","]":"]"}
    stack  = []
    for char in l:
        if(char in open):
            stack.append(char)
        elif(char in close):
            if(not stack ):
                return False
            elem = stack.pop()
            if(parent[char]!=elem):
                return False
        return False
    return not stack
# we are give a string s and we have to encrypt it
# a becomes z and b becomes y 
# s = input()
# atom = 'abcdefghijklm'
# zton = 'zyxwvutsrqpon'
# newstr = ''
# fmap = dict(zip(atom,zton))
# smap = dict(zip(zton,atom))
# for char in s:
#     if(fmap[char]):
#         newstr += fmap[char]
#     elif(smap[char]):
#         newstr += smap[char]
# print(newstr)


# givena a list and k no of rotation it has to make
# return the list after k rotation 
# def rotate(l,k):
#     for i in range(k):
#         last = l.pop()
#         l = [last]+l
#     for index in range(len(l)):
#         if(index != len(l)-1):
#             print(l[index],end=',')
#         else:
#             print(l[index])
# l = list(map(int,input('enter comma separated values:').split(',')))
# print(rotate(l,3))


def depth(s):
    start = '('
    end = ')'
    maxi = 0
    cd = 0
    for br in s:
        if(br == start):
            cd += 1
            maxi = max(cd,maxi)
        elif(br == end):
            cd -= 1
    return maxi

     
def depth(s):
    start = '('
    end = ')'
    maxi = 0
    cmax = 0
    for para in s:
        if para == start:
            cmax +=1
            maxi = max(cmax,maxi)
        elif(para == end):
            cmax -= 1
    return maxi



# given a two dimensional grid of n cross n and sequence of direction we have to find the final position by that sequence 
def position(words,n):
    x = 1 # start of x axis
    y = 1 # start of y axis

    xmax =  n
    xmin = 1
    ymax = n
    ymin = n

    for word in words:
        if word == 'N' and y+1 <= ymax:
            y+=1
        elif word == "S" and y-1 >= ymin:
            y -= 1
        elif word == "W" and x+1 <= xmax:
            x += 1
        elif word == "E" and x-1 >= xmin:
            x -= 1
    return (x,y) 

# function to take a matrix 
def cratematrix(n):
    m = []
    for i in range(n):
        row = list(map(int , input().split(',')))
        m.append(row)
    return m
def initialise(n):
    c = []
    for i in range(n):
        row = [0]*n
        c.append(row)
    return c
# sum of matrix
# we cannot perform any calculation like 
# simple arithematic calculation on the 
# matrix we have to initialise another 
# matrix c which will be the resultant
def matsum(a,b):
    c = initialise(3)
    for i in range(len(a)):
        for j in range(len(a)):
            c[i][j] = a[i][j] + b[i][j]
    return c
# now multiplictation of a matrix 

def matmul(a,b):
    dim = len(a)
    c = initialise(dim)
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                c[i][j] += a[i][k] * b[k][i]
    return c
# we have to create a even.csv 
def evengrid(m,n):
    f = open('even.csv','w') 
    elem = 2
    for i in range(m):
        line = ''
        for j in range(n-1):
            line = line + str(elem) +','
            elem += 2
        line = line + str(elem)+'\n'
        elem += 2
        f.write(line)
    f.close()
# print(evengrid(4,3))


def evengrid(m,n):
    elem = 3
    f = open('even.csv','w')
    for i in range(m):
        line = ''
        for j in range(n):
            if(j!=n-1):
                line += str(elem) + ','
            else:
                line += str(elem) +'\n'
            elem += 2 
        f.write(line)

    f.close()
# print(evengrid(4,3))

# we are given a list of students with their 
# name roll number and a sunject marks
# we have to create a txt file for everu
# student with their name as file name 
# and their grades inside


s = open('names.csv','r')
l = s.readlines()
def compute_grade(mark):
    if(mark >= 90):
        return 'S'
    elif(mark >= 80):
        return 'A'
    elif(mark >= 70):
        return "B"
    elif(mark >= 60):
        return 'C'
    elif(mark >= 50):
        return "D"
    elif(mark >= 40):
        return "E"
    else:
        return 'U'
#name,rollno,marks
for elem in l[1:]:
    man = elem.split(',')
    marks = int(man[-1].strip())
    grade = compute_grade(marks)
    name = man[0]
    roll = man[1]
    g1 = open(name+'.txt','w')
    g1.write(f'Dear {name} (rollno{roll}) you have secured {grade} grade.')
    g1.close()

with open('even.csv','r') as file,open('python.csv','w') as p:
    l = list(file)
    p.write(l[0])
    for line in l[1:]:
        w= line.strip().split(',')
        p.write(line)

def camel(s):
    l=s.split()
    final = ''
    for char in l:
        temp = ''
        c = char.lower()
        temp += c[0].upper()
        temp += c[1:]
        final += temp
    return final
print(camel('this is not going to be easy'))














