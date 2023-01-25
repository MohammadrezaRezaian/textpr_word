import vese

file = open('data.txt','r+')
data = file.read()

#num 1
def numtxt(data):
    words = data.split()
    print(vese.vi[2] %len(words) )

#num 2
def sea_word(data,w):
    if w in data.split():
        print(vese.vi[3])
    else :
        print(vese.vi[4])

#num 3
def cou_word(data,w):
    if w in data.split():
        ls = list(data.split())
        co = ls.count(w)
        print(vese.vi[6] %co)
    else :
        print('word not found')



def savd (data,old,new):    
    if old in data.split():
        with open('data.txt','r') as file:
            data = file.read()
            data = data.replace(old,new)
    
        m = input("save ==> y / n")

        if m == "y" or "Y" :
            with open('data.txt','w') as file:
                file.write(data)
        else :
            print("dont save")
    else:
        print("not find words")

