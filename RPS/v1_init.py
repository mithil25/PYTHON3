print("Welcome to Rock Paper and Scissors Game!\n")
print("Enter\n Rock...\n Paper...\n and Scissor...\n")
player1 = input("Player 1 make your move: ").lower()
while player1 not in ['rock', 'paper', 'scissor']:
    player1 = input("Enter Valid Move: ").lower()
print("NO CHEATING!\n"*30)
player2 = input("Player 2 make your move: ").lower()
while player2 not in ['rock', 'paper', 'scissor']:
    player2 = input("Enter Valid Move: ").lower()

winner = None
if player1 == player2:
    print("Its a Tie!\n")
elif player1 == 'rock' and player2 == 'scissor':
    winner = 'Player 1'
elif player1 == 'paper' and player2 == 'rock':
    winner = 'Player 1'
elif player1 == 'scissor' and player2 == 'paper':
    winner = 'Player 1'
else:
    winner = 'Player 2'

if winner:    
    print(f'Winner of the game is {winner}')