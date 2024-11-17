#This program simulates a race between a tortoise and hare


import random #allows program to generate random values
position = 1

#opening statement for program
print("ON YOUR MARK... GET SET...\nGO!!!!!!\nAND THEY'RE OFF!")

#determines where and by how much the tortoise moves
def tort_moves(position):
    num = random.randint(1, 10)
    if num >= 1 and num <= 5:
        return position + 3             #fast plod
    elif num >= 6 and num <= 7:
        return position - 5             #slip
    elif num >= 8 and num <= 10:
        return position + 1             #slow plod
    position
    if position < 1:
        return position == 1            #ensures tortoise will not go further back that the starting position


#determines where and by how much the hare moves   
def hare_moves(position):
    num = random.randint(1, 10)
    if num >= 1 and num <= 2:
        return position                 #sleep
    elif num >= 3 and num <= 4:
        return position + 7             #big hop
    elif num == 5:
        return position - 10            #big slip
    elif num >= 6 and num <= 8:
        return position + 1             #small hop
    elif num >= 9 and num <= 10:
        return position - 2             #small slip
    position
    if position < 1:
        return position == 1            #Ensures tortoise will not go further back that the starting position
    
#prints the designated letter at position of racer
def racers_positions(hare_now, tort_now):
    for i in range(0,51):
        if i == hare_now:
            if hare_now < 1:
                hare_now = 1
            print('H', end= '')
            continue
        if i == tort_now:
            if tort_now < 1:
                tort_now = 1
            print('T', end= '')
        else:
            print(' ', end= '')

    print()

def main():
    #creates empty track for the race
    track = [' ']*50            
    #starts tortoise and hare at position 1
    tort_now = 1
    hare_now = 1
    position = 1
    #starts timer at 0
    seconds = 0

    #connects the possible moves to the current position of the animal
    while tort_now < 50 and hare_now < 50:
        tort_now = tort_moves(tort_now)
        if tort_now < 1:
            tort_now = 1

        hare_now = hare_moves(hare_now)
        if hare_now < 1:
            hare_now = 1

        #prints OW if the animals have the same position
        if tort_now == hare_now:
            print('OW!!')

        #prints the letter for the new position
        racers_positions(hare_now, tort_now)

        #adds 1 second for each move done by both animals
        seconds += 1

    #declares the winner and time of race
    if tort_now >= 50:
        print('Tortoise wins!! Yay!')
    elif hare_now >= 50:
        print('Hare wins. Yay.')
    print('Time of race:', seconds, 'seconds.')



main()




