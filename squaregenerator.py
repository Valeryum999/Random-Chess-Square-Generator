import random

square_letter = ['a','b','c','d','e','f','g','h']
square_number = ['1','2','3','4','5','6','7','8']
correct_guesses = 0
total_guesses = 0

print('\nEnter 0 for white and 1 for black, CTRL+C when you have finished.\n')

try:
    while 1:
        square_letter_guess = random.randint(0,7)
        square_number_guess = random.randint(0,7)
        print(square_letter[square_letter_guess] + square_number[square_number_guess])

        if square_letter_guess%2==1 and square_number_guess%2==1:
            result = '1'
        elif square_letter_guess%2==0 and square_number_guess%2==0:
            result = '1'
        else:
            result = '0'

        print('White or Black : ')

        user_guess = input()

        if user_guess == result:
            correct_guesses = correct_guesses + 1
        total_guesses = total_guesses + 1
        if result =='1':
            print('Black')
        else:
            print('White')
        print()

except KeyboardInterrupt:
    if correct_guesses != 1:
        print('\nYou got ' + str(correct_guesses) + ' correct guesses out of ' + str(total_guesses))
    else:
        print('\nYou got ' + str(correct_guesses) + ' correct guess out of ' + str(total_guesses))
