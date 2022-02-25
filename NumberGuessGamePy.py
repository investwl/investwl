from random import randint
import pdb
rand = randint(1,100)
bb = 0
cc = 0
inputnya = 0
yes = "yes"
no = "no"
while True:
    aa = int(input("Guess a number from 1-100 : "))
    if(aa == rand):
        print("Correct! Congrats!")
        break
    elif(aa < rand):
        print("Too small!")
    else:
        print("Too big!")
    if(aa != rand):
        while True:
            inputnya = input("Try again (yes/no)? --> ")
            if(inputnya == yes or inputnya == no):
                break
            else:
                continue

    if(inputnya == yes):
        continue
    elif(inputnya == no):
        break
    
print("Byee")