def rockpaperscissor(player1,player2):
    if player1 == 'scissor' and player2 == 'paper':
        a='Player 1 wins'
    elif player1 == 'scissor' and player2 == 'rock':
        a='player 2 wins'
    elif player1 == 'scissor' and player2 == 'scissor':
        a='draw'
    elif player1 == 'rock' and player2 == 'paper':
        a = 'player 2 wins'
    elif player1 == 'rock' and player2 == 'scissor':
        a='Player 1 wins'
    elif player1 == 'rock' and player2 == 'rock':
        a='draw'
    elif player1 == 'paper' and player2 == 'scissor':
        a='player 2 wins'
    elif player1 == 'paper' and player2 == 'rock':
        a='Player 1 wins'
    elif player1 == 'paper' and player2 == 'paper':
        a='draw'
    else:
        a='INVALID INPUT'
    return a
player1 = input('PLAYER 1 :')
player2 = input('PLAYER 2 :')
print(rockpaperscissor(player1,player2))
