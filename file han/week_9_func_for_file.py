f = open('sample.txt','r')
s = f.readline() # it will read first line
print(f.readline())
everything = f.read() # reading the whole file but we should 
avoid because reading the whole file will cause memory lose
l = f.readlines() # it will read whole file and will return a list
g = list(f) # it will also return a list of all the elements of the file
print(g)
print(everything)
# we can only write string only we can convert anything in string

f = open('sample.txt','w')
f.write('ramani\n')
f.write('second\n')
f.write('third\n')
f.write('4')
 we can write string only not integers
f.writelines(['one\n','two\n','threee\n']) # here we can write lines in a file
f.close()


# ppa 
# reading line by line of a file with no extra spaces 

def read_file(filename):
    f = open(filename)
    for line in f:
        print(line.strip())
    f.close()
# reading the nth line of file 
def read_nline(filename,n):
    f = open(filename)
    g = f.readlines()
    if(len(g)<n):
        return None
    return g[n-1].strip()
# findig the maximum of a file line number
def get_max_line(filename):
    f = open(filename)
    l = list(f)
    f.close()
    num = []
    for x in l:
        num.append(int(x))
    return num.index(max(num))+1
# dealing with csv files

f = open('age.csv')
l = list(f)[1:] 
#it will convert the whole file into a list with
# each lines separately
# print(l)
f.close()
d = dict()
for lines in l:
    name,age = (lines.strip().split(','))
    d[name]=int(age)
print(d)

# function to convert a csv file into a dictionary
def csv_to_dict(filename):
    f = open(filename)
    l = list(f)[1:]
    f.close()
    d=dict()
    for x in l:
        name,age=x.strip().split(',')
        d[name]=int(age)
    return d
# function to turn a csv file into a matrix with dimesion d
def matrix(filename):
    f = open(filename)
    l = list(f)
    matrix = []
    for x in l:
        row = x.strip().split(',')
        for j in range(len(row)):
            row[j]=int(row[j])
        matrix.append(row)
    return matrix
print(matrix('mat.csv'))
        
# writing a file 
# wrining a open.txt fie of ap with d and first term and last term
def write_ap(a,d,n):
    f = open('out.txt','w')
    term = a
    for i in range(n):
        if(i != n-1):
            f.write(str(term)+'\n')
        else:
            f.write(str(term))
        term = term + d 
    f.close()
# print(write_ap(4,5,40))
    
def count_t():

    with open('story.txt','r') as f: 
        # f = open('story.txt','r') this is not the proper way because it has to be closed
        count = 0
        for line in f:
            if(line[0]!='T'):
                count += 1
        print(count)
    # f.close()\
# write a python function to display the total number of words in file 
def wordcount(filename):
    with open(filename) as f:
        w = f.read() #  this will read the whole file
        w.replace('\n',' ') # here all the new line characters gets removed and instead there we have white spaces
    return len(w.split())

# writig a definition to count the occurance of 'the'in the file
def find_the(filename):
    with open(filename) as f:
        w=f.read().replace('\n',' ')
        return w.count('the')
# writing a definition to display those words whose lenth is less than 4
def display_word(filename):
    with open(filename,'r') as f:
        w = f.read().replace('\n',' ').split()
        for word in w:
            if (len(word.strip())<4):
                print(word)
# function to find the number of words ending with alpahbet 'e'
def finde(filename):
    with open(filename,'r') as f:
        count = 0
        w = f.read().replace('\n',' ').split()
        for word in w:
            if(word[-1]=='e'):
                count += 1
    return count
# writing function to add a hash symbol after every character in a string
def hash_display(filename):
    with open(filename,'r') as f :
        w = f.read().replace('\n',' ').split()
        for word in w:
            new = ''
            for char in word.strip():
                new += char + '#'
# function to find the longesst word of a file 
def find_longest(filename):
    with open(filename,'r') as f:
        w = f.read().replace('\n',' ').split()
        most = set()
        maxi = 0
        for word in w:
            if(len(word)>maxi):
                most.add(word)
                maxi = len(word)
            elif (len(word)==maxi):
                most.add(word)
    return most

# function to find the frequency of each words in a file       
def get_frequency(filename):
    with open(filename,'r') as f,open('out.txt','w') as o:
        w = f.read().replace('\n',' ').split()
        freq = dict()
        for word in w:
            freq[word] = freq.get(word,0)+1
        for i ,(k,v) in enumerate(freq.items()):
            line = str(k) + '-->' + str(v)
            if i != len(freq)-1:
                line += '\n'
            o.write(line)
print(get_frequency('test.txt'))
