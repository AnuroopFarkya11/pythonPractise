import random

def rollDice():
    min_value = 1 
    max_value = 6

    res = random.randint(min_value,max_value)
    return res



print("ROLL A DICE : HIT ENTER TO GET A NUMBER")

ch = ''

while(ch != 'x'):
    result = rollDice()
    print("Dice rolled : ", result )
    ch = input()

