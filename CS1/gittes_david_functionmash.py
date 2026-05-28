import random 

def chorus(): #define function that displays chorus
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''
    print('''And all the roads we have to walk are winding  
And all the lights that lead us there are blinding
There are many things that I would like to say to you
But I don't know how''') #print verse
    print('''Because maybe'
You're gonna be the one that saves me
And after all
You're my wonderwall''') #print verse
   
def verse_1(): #define function that displays verse number 1
   '''
    Prints the first verse of a song
    Args:
        None
    Returns:
        print: first verse
   '''
   print ('''Today is gonna be the day
That they're gonna throw it back to you
By now, you should've somehow
Realised what you gotta do
I don't believe that anybody
Feels the way I do about you now''') #print verse

def sing_song ():  #define function
   '''
    Uses first verse function and chorus function to sing a song
    Args:
        None
    Returns:
        print: entire song
   '''
   verse_1 () #execute function
   print('''Backbeat, the word is on the street
That the fire in your heart is out
I'm sure you've heard it all before
But you never really had a doubt
I don't believe that anybody
Feels the way I do about you now''') #print verse
   chorus() #execute chorus function
   verse_1() #execute verse function
   chorus() #execute chorus function

def add(number_1, number_2):
    '''
    Takes two numbers and adds them together
    Args:
        number_1 (int): first number
        number_2 (int): second number
    Returns:
        print: sum of the two numbers
    '''
    res = number_1 + number_2
    print(f'{res}')

def print_list(array):
    '''
    Takes a list and prints every element in that list individually (vertically)
    Args:
        array (list): 
    Returns:
        print: list vertically
    '''
    for element in array:
        print(element)

def in_list(array, element):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args:
        array (list)
        element (any)
    Return:
        bool: true if element is in array
    '''
    return element in array

def is_integer(test_number):
    '''
    Takes any parameter and returns a boolean based on if it is an integer
    Args:
        test_number (int)
    Return:
        bool: true if test_number is an integer
    '''
    try:
        int(test_number)
        return True
    except ValueError:
        return False

def get_integer():
    '''
    Asks the user for a number, uses is_integer to check input, returns the integer
    Args:
        None
    Return:
        number (int): the number that user entered converted into an integer
    '''
    while True:
        number = input('Enter a Number: ')

        if is_integer(number):
            return int(number)
        else:
            print('Enter an integer')

def get_random():
    '''
    Uses get_integer and prints a random number between two integers
    Args:
        None
    Return:
        print: a random number between the two given integers
    '''
    number_1 = get_integer()
    number_2 = get_integer()#use get_integer to get number2
    if number_1 < number_2: #if number1 < number2:
        print(random.randint(number_1, number_2))#print random integer between number1 and number2
    else: #else:
        print(random.randint(number_2, number_1)) #print random integer between number2 and number1

def count_vowels(string):
    '''
    Takes a string and returns the number of vowels in it
    Args:
        string (str)
    Return:
        count (int): total number of vowels
    '''
    vowels = ['a', 'e', 'i', 'o', 'u'] #list of vowels
    count = 0 #count = 0

    for char in string: #for every char in string:
       if char in vowels: #if char is in vowels
            count += 1#add one to count
    return count #return count

def reverse_string(string):
    '''
    Takes a string and reverses it
    Args:
        string (str)
    Return:
        str: the original string reversed 
    '''
    return string[::-1]
def is_palindrome(palindrome):
    '''
    Takes a string and checks whether it is a palindrome
    Args:
        palindrome (str)
    Return:
        bool: True if palindrome is a palindrome
    '''
    return palindrome == reverse_string(palindrome)

def get_initials(fullname):
    '''
    Takes a name and returns the initials
    Args:
        fullname (str)
    Return:
        initials (str): the initials of the fullname
    '''
    name_list = fullname.split() #use the split function to split fullname into a list of names (look up split in python)
    initials = '' #set initials to blank string

    for name in name_list: #for every name in list of names:
        initials += name[0] #add first letter of name to initials 
    return initials  #return initials

def replace_character(string, old_character, new_character):
    '''
    Takes a string, an old character, and a new character, and replaces every instance in the string of the old character with the new 
    Args:
        string (str)
        old_character (str)
        new_character (str)
    Return:
        new_string (str): the original word with the old character replaced by the new character
    '''
    new_string = ''
    for char in string:#for every char in string:
        if char == old_character: #if char equals old_character:
            new_string += new_character  #add new_character to new_string
        else: #else:
            new_string += char #add char to new_string
    return new_string

def word_scramble():
    '''
    Randomly selects a word to scramble from the list, and gives the user 5 guesses to correctly enter the pre-scrambled word
    Args:
        none
    '''
    word_list = ['scramble', 'antarctica', 'astronaut', 'silk', 'quick', 'scissors'] #create a list of words
    selected_word = random.choice(word_list) #computer randomly chooses the word
    word = list(selected_word)
    random.shuffle(word) #random.shuffle
    print(f'{"".join(word)}') #print shuffled word

    guesses = 0 #give user 5 guesses
    
    while guesses < 5: 
        guess = input('What is the unscrambled word? (You have 5 guesses)').lower() #if user's guess = computer's chosen word
        
        if guess == selected_word:
            print('You got it!')
            break
        else: 
            print('try again!')
            guesses += 1

def main():
    while True:
        which_one = input('''Choose the number that corresponds with the function to perform from this list (Enter "q" to quit): 
1. sing 
2. add
3. print list
4. in list
5. is integer
6. get integer
7. get random
8. count vowels
9. reverse string 
10. return palindrome
11. get initials
12. replace character 
13. word scramble game\n''')
        
        if which_one == 'q':
            break
        elif which_one == '1':
            sing_song()
        elif which_one == '2':
            number_1 = get_integer()
            number_2 = get_integer()
            add(number_1, number_2)
        elif which_one == '3':
            user_list = input('enter list (separate items by comma)').split(',')
            print_list(user_list)
        elif which_one == '4':
            user_list = input('enter list (separate items by comma)').split(',')
            element = input('Enter an item to check if it is in your list')
            print(in_list(user_list, element))
        elif which_one == '5':
            check_number = input('Enter a number')
            if is_integer(check_number):
                print('That is an integer')
            else:
                print('That is not an integer')
        elif which_one == '6':
            num = get_integer()
            print(f'Your number is {num}')
        elif which_one == '7':
            get_random()
        elif which_one == '8':
            string = input('Enter a word')
            count = count_vowels(string)
            print(f'{count} is the number of vowels in your word')
        elif which_one == '9':
            string = input('Enter a word that you wished to be reversed')
            print(f'{reverse_string(string)}')
        elif which_one == '10':
            palindrome = input('Enter a palindrome to be checked')
            print(f'{palindrome} is a palindrome? True/False: {is_palindrome(palindrome)}')
        elif which_one == '11':
            fullname = input('Enter your full name')
            print(f'{get_initials(fullname)}')
        elif which_one == '12':
            phrase = input('Enter a phrase that you wish to be altered')
            old_character = input('Enter a character in your phrase that you wish to be switched')
            new_character = input('Enter a character to switch into your phrase')
            new_phrase = replace_character(phrase, old_character, new_character)
            print(f'Your new phrase is {new_phrase}')
        elif which_one == '13':
            word_scramble()
        else:
            print('Please enter a number that corresponds with the desired function that you want to perform (Enter "q" to quit)')
main()