import msvcrt
import random

#random
def random_position():
    return (random.randint(0,20)),(random.randint(0,20))

#Snake-bane
bredde = 50
højde = 50

#slange
slangehoved = (10,10)
slangekrop = [(11,10)]

#frugt
frugt = [random.randint]

#vis bane




num = 0
done = False
while not done:
    print(num)
    num += 1

    if msvcrt.kbhit():
        print("you pressed",msvcrt.getch(),"so now i will quit")
        done = True
