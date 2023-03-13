import msvcrt
import random

#random
def random_position():
    return (random.randint(0,20)),(random.randint(0,20))

#Snake-bane
bredde = 20
højde = 20

#slange
slange = (10,10)
slangekrop = (11,10)

#frugt
frugt = [random.randint]

#bevægelse
retning 



num = 0
done = False
while not done:
    print(num)
    num += 1

    if msvcrt.kbhit():
        print "you pressed",msvcrt.getch(),"so now i will quit"
        done = True