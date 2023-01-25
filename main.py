
import vese
import clad

print(vese.vi[1])

num_ls = input("----------------------- Pleas Enter (?) ")
ls = [1,2,3,4]

while True:
    if int(num_ls) in ls:
        print(num_ls)

        #num 1 
        if int(num_ls) == 1:
            clad.numtxt(clad.data)

        #num 2
        if int(num_ls) == 2:
            x = input(vese.vi[5])
            clad.sea_word(clad.data,x)
        
        #num 3
        if int(num_ls) == 3 :
            x = input(vese.vi[5])
            clad.cou_word(clad.data,x)
        
        #num 4
        if int(num_ls) == 4:

            oldm = input(vese.vi[7])
            newm = input(vese.vi[8])
            clad.savd(clad.data,oldm,newm)
        break
    else:
        print("out of rang")
        break