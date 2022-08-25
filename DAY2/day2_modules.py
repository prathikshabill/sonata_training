#PALINDROME
def pal(a):
    a = input('Give input: ')
    if a==a[::-1]:
        b='PALINDROME'
        return b
    else:
        c='NOT PALINDROME'
        return c



#rock paper scissor
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
#player1 = input('PLAYER 1 :')
#player2 = input('PLAYER 2 :')
#print(rockpaperscissor(player1,player2))

#WORD COUNT
def wordcount(word):
    length = len(word.split())
    return length
#print(wordcount('rock paper scissor'))

#GREATEST  OF 3 NO
def greatest(num1,num2,num3):
    num1 = int(input('Enter 1st number: '))
    num2 = int(input('Enter 2nd number: '))
    num3 = int(input('Enter 3rd number: '))
   # print(greatest(num1, num2, num3))
    if (num1 > num2) and (num1 > num3):
        a=num1
    elif (num2 > num3) and (num2>num1):
        a=num2
    else:
        a=num3
    return a



#AGE
def agecal(n):
    a=100-n
    b=2022+a
    return a,b
#print(agecal(32))
