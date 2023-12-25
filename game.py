import random 
def gamewin(comp,you):
    if comp==you:
        print("Its a TIE")
    elif comp=='R':
        if you=='P':
            print("you win :>")
        elif you=='S':
            print("you lose :< ")
    elif comp=='P':
        if you=='S':
            print("you win :>")
        elif you=='R':
            print("you lose :< ")
    elif comp=='S':
        if you=='R':
            print("you win :>")
        elif you=='P':
            print("you lose :< ")                        

comp = print("Computer's turn : Rock(R) Paper(P) Sicssor(S)")
a = random.randint(1,3)
if a==1:
    comp = 'R' 
elif a==2:
    comp = 'P'
elif a==3:
    comp = 'S' 

you = input("Your turn : Rock(R) Paper(P) Scissor(S)\n")

print(f"computer has choosen  {comp}")
print(f"you choose  {you}")

gamewin(comp,you)

