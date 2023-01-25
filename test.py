import imp


import clad

num = 4
if num == 4 :
    old = input("old")
    new = input("new")
    if old in clad.data.split():
        with open('data.txt','r') as file:
            data = file.read()
            data = data.replace(old,new)
    
        m = input("save : yes // no")

        if m == "y" or "Y" :
            with open('data.txt','w') as file:
                file.write(data)
        else :
            print("dont save")
    else:
        print("not find words")

