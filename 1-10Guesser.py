import random 

answer = input('Do you want to play? ')

while answer.lower() == 'yes':
    random_number_out_of_ten = random.randint(1,10)
    user_num = int(input('Enter a number between one and 10: '))

    if random_number_out_of_ten == user_num:
        print('You guessed correct.')
        answer = input('Do you want to play again?')

    elif random_number_out_of_ten >= user_num:
        difference = random_number_out_of_ten - user_num
        print('You guessed too low by %d.' % (difference))
        answer = input('Do you want to play again? ')

    elif random_number_out_of_ten <= user_num:
        difference = user_num - random_number_out_of_ten
        print('You guessed too high by %d.' % (difference))
        answer = input('Do you want to play again? ')
        
    else:
        print('What are you even trying to do?')
        answer = input('Do you want to play again? ')

print(random_number_out_of_ten)

