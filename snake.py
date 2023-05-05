import msvcrt
import random
import time
import os

#random
def random_position():
    return (random.randint(0,20)),(random.randint(0,20))

#Snake-bane
bredde = 20 #integer
højde = 20

#slange
slangehoved = (10, 10) #tuple

slangekrop = [(11,10)] #liste

#frugt
frugt = (random.randint(0, bredde-1),random.randint(0, højde-1))

#score
score = 0

#baneloop
done = False #boolean
currentTime = 0
previousTime = 0
interval = 500
input = "a" #string
while not done:
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        if ch == b'w':
            input = "w"
        elif ch == b'a':
            input = "a"
        elif ch == b's':
            input = "s"
        elif ch == b'd':
            input = "d"

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
                elif (x, y) in slangekrop:#[0][0] == x and slangekrop[0][1]==y:
                    print ("H",end= " ")
                elif frugt[0]== x and frugt[1]== y:
                    print("§", end = " ")
                else:
                    print(".", end = " ") 
        #bevæg slange
        if slangehoved == frugt:
            frugt = (random.randint(0, bredde-1),random.randint(0, højde-1))
            score = score + 1
        else:
            slangekrop.pop()
        slangekrop.insert(0,slangehoved)

        (x, y) = slangehoved
        if input == "w":
            slangehoved = (x, y-1)
        elif input == "a":
            slangehoved = (x-1, y)
        elif input == "s":
            slangehoved = (x, y+1)
        elif input == "d":
            slangehoved = (x+1, y)
        print(f"score {score}")
