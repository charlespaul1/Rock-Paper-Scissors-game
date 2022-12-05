from random import randint
#creating play options
m = ['Rock', 'Paper', 'Scissors']
#asssign a random play to the computer
computer = m[randint(0,2)]
#setting player to false
player = False

while player == False:
    #set player to true
    player = input('Rock, Paper, Scissors: ')
    if player == computer:
        print("Tie!!!!")
    elif player == 'Rock':
        if computer == 'Paper':
            print('You looose', player, 'covers', player)
        else:
            print('You wiiiiin!!',player,'smashes',computer)
    elif player == 'paper':
        if computer == 'scissors':
            print('you loose',computer,'cuts', player)
        else:
            print('you win', player, 'covers', computer)
    elif player == 'scissors':
        if computer == 'Rock':
            print('you loose...', computer, 'smashes', player)
        else:
            print('you win', player, 'cut',computer)
    else:
        print('thats not a valid play..check your spelling')
    #the player was set to true, nut we want it to be false so that the loop continues
    player = False
    computer = m[randint(0,2)]