'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using
input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

'''

gameOn = True

while gameOn:
    playerOne = input('Player1 - Rock, paper or scissors?: ')
    playerTwo = input('Player2 - Rock, paper or scissors?: ')
    while playerOne == 'Rock':
        if playerTwo == 'Rock':
            print('Draw! Try again!')
            break
        elif playerTwo == 'Scissors':
            again = input('Player 1 Win! - %s beat %s Do you want play again?: '\
                        %(playerOne, playerTwo))
            if again == 'y':
                break
            else:
                print('See You!')
                gameOn = False
                break
        else:
            again = input('Player 2 Win! - %s beat %s Do you want play again?: '\
                          %(playerTwo, playerOne))
            if again == 'y':
                break
            else:
                print('See You!')
                gameOn = False
                break
print('end')
        


    
