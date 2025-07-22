# file = open('new.txt','w')
# for i in range(1,101):
#     file.write(str(i)+' ')
# file.close()


file2 = open('new.txt','r')
file2.read()
for value in file2:
    print(value)
file2.close()