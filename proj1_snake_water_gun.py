import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp,you):

# If two values are equal, declare same
    if comp == you:
        return None

# Check for all possibilities when computer choose s
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False

# Check for all possibilities when computer choose w
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

# Check for all possibilities when computer choose g
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False


print("Computer's Turn: Snake(s), Water(w) or Gun(g)?")
randNo = random.randint(1,3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you= input("Your Turn: Snake(s), Water(w) or Gun(g)?")
a=gameWin(comp,you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a == None:
    print("The Game is Tie!!")

elif a:
    print("You Win!!!")

else:
    print("You Loose!!!")