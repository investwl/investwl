from queuedatastructure import *

while True:
    mintakal = input("Input a sentence to check if it is a palindrome or not\n(Palindrome only works on odd length word!)\n--> ")
    panjangkal = len(mintakal)
    panjg = panjangkal // 2

    mintakal = list(mintakal)

    for i in range (0,panjangkal-1):
        enqueue(mintakal[i])

    if panjangkal > 1:
        while True:
            for i in range(0,panjg):
                if(mintakal[i] == mintakal[panjangkal-1]):
                    dequeue()
                    panjangkal = panjangkal - 2
                    panjg = panjg - 1
                else:
                    print("Not a palindrome.")
                    break
                if(panjangkal == panjg):
                    print("Indeed a palindrome.")
                    break
                else:
                    True
                panjangkal = panjangkal - 1

            break

        while True:
            play_again = input("Play again? (Yes / No)\n--> ")
            if play_again == "yes" or play_again == "Yes" or play_again == "no" or play_again == "No":
                break
            else:
                print("Yes or no answer only!")
                continue

        if play_again == "yes" or play_again == "Yes":
            True
        elif play_again == "no" or play_again == "No":
            print("Goodbye ! Thanks for playing !")
            exit()