import random

name = input('What is your name?')
print (f'Good Luck {name}!')

while True:
    number = random.randint(1, 10)
    guesses = 5
    correct = 0
    rounds = 0

    while guesses > 0:
        try:
            guess = int(input("Please enter an integer between 1 and 10: "))

            if 1 <= guess <= 10:  
                break  
            else:
                print("Please enter a number between 1-10")
        except ValueError:
                print("Please enter a whole number between 1-10")
        if guess == number: 
            print('You got it!')
            correct += 1
            break
        elif guess > number: 
            print('Your number is too high')
        else: 
            print('Your number is too low')
        guesses -= 1

    if guesses == 0:
        print ('You lost this round')
        
    rounds += 1

    while True:
        play_again = input('Do you want to play again').lower()
        
        if play_again == 'no':
            exit()
        elif play_again == 'yes': 
            break
        else: 
            print('Please enter yes or no')

