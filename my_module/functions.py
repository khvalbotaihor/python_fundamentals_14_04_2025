
def greeting_9():
    print("Hello, world!")


def greeting_10(name):  
    print(f"Hello, {name}!")



def user_guessing_game(secret_num, stop_chars):
    user_input = ''
    while user_input != stop_chars:
        user_input = input('\n\n\n\nGuess a number from 0 to 100: ')
        if user_input == secret_num:
            print('You guessed the number!')
        print(f'Your number is {user_input}, please try another one!')


name = "functions"
# This is a comment\
class Test:
    a = 66