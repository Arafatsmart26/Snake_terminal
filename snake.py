import msvcrt
import random
import time
import os

#random
def random_position():
    return (random.randint(0,20)),(random.randint(0,20))

#Snake-bane
bredde = 30
højde = 30

#slange
slangehoved = (10,10)
slangekrop = [(11,10)]

#frugt
frugt = [random.randint]

#mainloop
done = False
currentTime = 0
previousTime = 0
interval = 500
while not done:
    
    currentTime = time.perf_counter() * 1000
    if currentTime - previousTime > interval:
        os.system("cls ")
        previousTime = currentTime
        #vis bane
        for y in range(højde):
            print("")
            for x in range(bredde):
                if slangehoved[0]== x and slangehoved[1]== y:
                    print("@", end = " ")
                elif slangekrop[0][0] == x and slangekrop[0][1]==y:
                    print ("H",end= " ")
                else:
                    print(".", end = " ")
    

    if msvcrt.kbhit():
        ch = msvcrt.getch()
        if ch == b'd':
            
        print("you pressed",msvcrt.getch(),"so now i will quit")
        done = True
