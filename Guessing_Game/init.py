from random import randint

def get_player_want_to_quit():
    player_input = input("Do you want to keep playing (yes/no) ?\n")
    return player_input.lower() == "no"
    
def init_game():
    do_player_want_to_quit = False
    no_guessed = randint(1,10)
    print("Welcome to Guess Game Enter your guess between 1 to 10")
    while not do_player_want_to_quit:
        player_guess = int(input("Enter your guess\n"))
        if player_guess == no_guessed:
            print("Your guessed matched")
            do_player_want_to_quit = get_player_want_to_quit()
            if not do_player_want_to_quit:
                no_guessed = randint(1,10)
        elif player_guess > no_guessed:
            print("Your guessed no is higher") 
        else:
            print("Your guessed no is lower")
    print("Thanks for playing. Bye!")
init_game()
    