# a = 0

# while a < 10:
#     print(f'Hello {a}')
#     a += 1


# for a in range(10):
#     print(f'Hello {a}')
#     a += 1
# The while loop is not the best way to iterate over a range of numbers    


user_input = ''
while user_input != '-1':
    user_input = input('Guess a number from 0 to 100: ')
    if user_input == '77':
        print('You guessed the number!')
    print(f'Your number is {user_input}, please try another one!')
