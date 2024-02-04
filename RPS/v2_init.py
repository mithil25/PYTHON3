from random import choice

def input_from_player():
    print(".............. Enter Rock, Paper & Scissor .............\n")
    player = input("Player make your move: ").lower()
    while player not in ['rock', 'paper', 'scissor']:
        player = input("Enter Valid Move: ").lower()
    return player

def get_winner_of_the_game(player_move,computer_move):
    winner = None
    if player_move == computer_move:
        print("This round is a tie!")
        return "Tie"
    elif player_move == 'rock' and computer_move == 'scissor':
        winner = 'Player'
    elif player_move == 'paper' and computer_move == 'rock':
        winner = 'Player'
    elif player_move == 'scissor' and computer_move == 'paper':
        winner = 'Player'
    else:
        winner = 'Computer'
    
    if winner:
        print(f'Winner of the round is {winner} :- Player move is {player_move.upper()} and Computer move is {computer_move.upper()}')
    else:
        print(f'This round is a tie!')
    
    return winner

def init_game():
    player_win_count = 0
    computer_win_count = 0
    print("................ Welcome to Rock Paper and Scissors Game! ..................\n")
    total_no_of_rounds = int(input("How many rounds do you want to play?\n"))
    min_no_of_round_to_win = total_no_of_rounds/2+1
    no_of_rounds = 0
    if total_no_of_rounds <= 0:
        total_no_of_rounds = int(input("Please enter the valid no of rounds!"))
    while True:
        no_of_rounds += 1
        winner = get_game_winner()
        if winner.lower() == 'player':
            player_win_count += 1
        elif winner.lower() == 'computer':
            computer_win_count +=1 
    

        if player_win_count >= min_no_of_round_to_win or computer_win_count >= min_no_of_round_to_win or no_of_rounds >= total_no_of_rounds:
            break
        
    winner = 'NA'
    if player_win_count > computer_win_count:
        winner = 'Player'
    elif player_win_count < computer_win_count:
        winner = 'Computer'
    else:
        winner = 'Tie'
    print(f'\n ........... Winner of the GAME is {winner} :- Player win stats is {player_win_count} and Computer win stats is {computer_win_count} ........... \n')
    
def get_game_winner():
    player_move = input_from_player()
    valid_moves = ['scissor', 'paper', 'rock']
    computer_move = choice(valid_moves)
    winner = get_winner_of_the_game(player_move, computer_move)
    
    
    
    return winner

if __name__ == '__main__':
    init_game()