player1 = input('PLAYER 1 :')
player2 = input('PLAYER 2 :')
if player1 == 'scissor' and player2 == 'paper':
    print("Player 1 wins")
elif player1 == 'scissor' and player2 == 'rock':
    print("player 2 wins")
elif player1 == 'scissor' and player2 == 'scissor':
    print("draw")
elif player1 == 'rock' and player2 == 'paper':
    print("player 2 wins")
elif player1 == 'rock' and player2 == 'scissor':
    print("player 1 wins")
elif player1 == 'rock' and player2 == 'rock':
    print("draw")
elif player1 == 'paper' and player2 == 'scissor':
    print("player 2 wins")
elif player1 == 'paper' and player2 == 'rock':
    print("player 1 wins")
elif player1 == 'paper' and player2 == 'paper':
    print("draw")
else:
    print("INVALID INPUT")
