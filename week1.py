

# learning to import library 

# from datetime import datetime , timedelta
# name1=input()
# date1 = str(input())
# name2=input()
# date2=str(input())
# date1int=datetime.strptime(date1,"%d-%m-%Y")
# date2int=datetime.strptime(date2,"%d-%m-%Y")
# larrger=max(name1 , name2)
# if(date1int > date2int):
#     print(name1)
# elif(date2int > date1int):
#     print(name2)
# elif(date1int == date2int):
#     if(name1 > name2):
#         print(name1) 
#     else:"
#         print(name2)

# question : changing into uppercase 
# word="ram"
# uper= word.upper()
# print(uper)
# qustion: string validaton (given a sentence we have to check it on these conditons)
# word= input()
# flag=1
# first =(word[0])
# if (not(first.isalpha())):
#     flag=0
# if(len(word)<8 or len(word)>32):
#     flag=0
# if( "/" in word):
#     flag=0
# if('\\' in word):
#     flag=0
# if("'" in word):
#     flag=0
# if('"' in word):
#     flag=0
# if('=' in word):
#     flag=0
# if('='in word):
#     flag=0
# if(" " in word):
#     flag=0
# if(flag == 1):
#     print(True)   
# else:
#     print(False)    


# question: checking for sandwitch or plain text 

# num = input("enter a number:")
# first, middle, last = int(num[0]), int(num[1]), int(num[2])
# if first + last == middle:
#     print('sandwich')
# else:
#     print('plain')


# casa= False or True or False
# print(casa)

# question : palying with string slicing 
# kaka=input()
# kabra=len(kaka)
# if(kabra % 2 == 0):
#     if((kaka[-1])!="."):
#         kaka += "."
#     else:
#         kaka -= "."
# mid=(kabra+1)/2
# substring=""
# substring=kaka[mid]
# substring += kaka[mid+1]
# substring += kaka[mid+2]
# print(substring)


# qustion: count the number of words in a sentence or finding the number of space in the sentence 

# sentence=int(input())
# space=" "
# num=sentence.count(space)
# print(num)

# qustion : checking a string having number of open bracket is equalt to the number of closed brackets 
# word = input()
# match = False
# if word.count('(') == word.count(')'):
#     if word.count('[') == word.count(']'):
#         if word.count('{') == word.count('}'):
#             match = True
# if match:
#     print('PERFECT!')
# else:
#     print('IMPERFECT!')




# x=float(input())     
# if(x >= 0):
#     decrease=int(x)
#     if(decrease == x):
#         increase=decrease
#     else:
#         increase = decrease + 1
# elif(x < 0):
#     decrease = int(x)
#     if(decrease == x ):
#         increase=decrease
#     else:
#         increase= decrease - 1
# print(decrease)                    
# print(increase)


# question : checking for the winner of two teams who has scored more or who is the winner 


# team_a_score_first=input()
# team_a_wicket_first=input()
# team_a_score_second=input()
# team_a_wicket_second=input()

# team_b_score_first=input()
# team_b_wicket_first=input()
# team_b_score_second=input()
# team_b_wicket_second=input()

# team_a_total_score = team_a_score_first + team_a_score_second
# team_b_total_score = team_b_score_first + team_b_score_second

# if(team_a_total_score > team_b_total_score):
#     print('TEAM A')
# elif(team_b_total_score > team_a_total_score):
#     print("TEAM B")
# else:
#     print("DRAW")   

# question : palying with string with vowels 
# word= input()
# perfect=False
# if("a" in word and "e" in word and "i"in word and "o" in word and "u" in word):
#     if(word.index("a")< word.index("e")<word.index("i")<word.index("o")<word.index("u")):
#         if(word.count("a")>= word.count("e")>= word.count("i") >= word.count("o") >= word.count("u")):
#             perfect=True
# if(perfect):
#     print("perfect word")
# else:
#     print("not perfect")

        







