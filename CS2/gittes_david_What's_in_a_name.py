"""
┌───────────────────────────────────────────────────────────────────────────┐
│                            What's In a Name                               │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: David Gittes                                                        │
| Course: CS2                                                               |
| Date: September 30, 2025                                                  |
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description:  Interactive program that asks users for a name and then     |
|  presents a menu for the user to analyze their name and modify it in      |    
|  various methods.                                                         |
| Bonuses:                                                                  |
|    Subtotals of each consonant and vowel, Returnes full-name as a sorted  |
|    array of characters, A menu for users to navigate different options,   |
|    Returns boolean if name contains a title/distinction                   |
└───────────────────────────────────────────────────────────────────────────┘
"""
import random
def reverse_display(name):
    '''takes a string and reverses it
    
    args: name (str): name of user
    
    returns: (str): reversed name'''

    return name[::-1]

def lower_case(name):
    '''takes a string and makes all of the characters lowercase
    
    args: name (str): name of user
    
    returns: (str) name of user in lowercase'''
    new_name = ''

    for c in name:
        if 90 >= ord(c) >= 65:
            new_name += chr(ord(c) + 32)
        else:
            new_name += c
    return new_name

def upper_case(name):
    '''takes a string and makes all of the characters uppercase
        
        args: name (str): name of user
        
        returns: (str) name of user in uppercase'''
    new_name = ''

    for c in name:
        if 122 >= ord(c) >= 97:
            new_name += chr(ord(c) - 32)
        else:
            new_name += c
    return new_name        

def vowel_counter(name):
    '''counts the number of vowels in a word
        
    args: name (str): name of user
            
    returns: (int): the total count and subcounts for vowels in a name'''
    string = lower_case(name)
    count = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0 }

    for char in string:
        if char in count.keys():   #if character is in count dictionary 
            count[char] += 1       #add 1 to that characters count
    return count

def consonant_counter(name):
    '''counts the number of consonants in a word
        
    args: name (str): name of user
            
    returns: (int): the total count and subcounts for vowels in a name'''
    lowered = lower_case(name)
    count = {
    'b' : 0,
    'c' : 0,
    'c' : 0,
    'd' : 0,
    'f' : 0,
    'g' : 0,
    'h' : 0,
    'j' : 0,
    'k' : 0,
    'l' : 0,
    'm' : 0,
    'n' : 0,
    'p' : 0,
    'q' : 0,
    'r' : 0,
    's' : 0,
    't' : 0,
    'v' : 0,
    'w' : 0,
    'x' : 0,
    'y' : 0,
    'z' : 0, }

    for char in lowered:
        if char in count.keys():        #if character is in count dictionary
            count[char] += 1            #add 1 to that characters count
    return count

def name_seperator(name):
    '''Takes a name and seperates the name into individual words

    args: name (str): name of user
    
    returns: (list): a list that consists of the parts of user's full name'''
    names = []
    current_name = ''

    for char in name:
        if char == " ":
            names.append(current_name)
            current_name = ''
        else:
            current_name += char
    names.append(current_name)
    return names

def first_name(name):
    '''Takes user's full name and isolates the first name
    
    args: name (str): name of user
    
    returns: (str): first name of user'''
    names = name_seperator(name)
    return names[0]
def middle_name(name):
    '''Takes user's full name and isolates the middle name
    
    args: name (str): name of user
    
    returns: (str): middle name of user'''
    names = name_seperator(name)
    middle_names = names[1:-1]
    middle = ''
    for m in middle_names:
        middle += m + ' '
    return middle

def last_name(name):
    '''Takes user's full name and isolates the last name
    
    args: name (str): name of user
    
    returns: (str): last name of user'''
    names = name_seperator(name)
    return names[-1]

def last_hyphen_checker(name):
    '''Takes user's last name and check's if there is a hyphen

    args: name (str): name of user
    
    returns: (bool): True or False based on if the last name has a hyphen'''
    last = last_name(name)
    return "-" in last

def scramble_name(name):
    '''Takes a string and scrambles the word
    
    args: name (str): name of user
    
    returns: (str): scrambled name'''
    name = list(name)
    scrambled_name = ''

    while name:
        index = random.randint(0, len(name)-1)
        scrambled_name += name[index]
        name.pop(index)
    return scrambled_name

def palindrome_checker(name):
    '''Check's if user's name is a palindrom
    
    args: name (str): name of user
    
    returns: (bool): True or False based on if name is a palindrome'''
    return name == reverse_display(name)

def join_function(str_list):
    '''Takes a list and turns it into a string

    args: str_list (list): any list
    
    returns: (str): list turned into string'''
    string = '' 
    for e in str_list:
        string += e
    return string

def initial(name):
    '''Takes user's name and returns their initials
    
    args: name (str): name of user
    
    returns: (str): initials of user's name'''
    initials = ''

    for n in name_seperator(name):
        initials += n[0]
    return initials


def sort(name):
    '''Takes user's name and sorts the characters in alphabetical order
    
    args: name (str): name of user
    
    returns: (str): the user's name sorted in alphabetical order'''
    orig = lower_case(name)
    sorted = ['a']
    ascii_list = [97]
    #going through each letter and ascii value and moving the letter forwards until it is greater than the next letter
    for letter in orig:
        if letter == ' ':
            continue                 
        for i in range(len(ascii_list)):       
            if ord(letter) >= ascii_list[i]:     
                index = i + 1 
    #insert the letter and it's ascii value in the parrallel array             
        sorted.insert(index, letter)
        ascii_list.insert(index, ord(letter))
    return join_function(sorted[1::])

def title_checker(name):
    '''Takes a name and checks if the name has a title or distinction
    
    args: name (str): name of user
    
    returns: (bool): True or False based on if the user's name has a title in the first name'''
    titles = ['Dr.', 'Sir', 'Esq', 'Ph.d']
    first = first_name(name)
    for e in titles:
        if e in first:
            return True
    return False
def main():
    name = input("Enter your full name: ")
    while True:
        q = input('''What would you like to perform? (enter the number corresponding with your desired function, and q to quit)' 
        '1. Name Reverser ' 
        '2. Vowel Counter' 
        '3. Consonant Counter' 
        '4. First Name Checker' 
        '5. Last Name Checker' 
        '6. Middle Name Checker' 
        '7. Last Name Hyphen Checker' 
        '8. Lowercase Function' 
        '9. Uppercase Function'
        '10. Name Scrambler '
        '11. Palindrome Checker'
        '12. Sort Function
        '13. Initials Function
        '14. Title/Distinction Checker
        ''')
        if q == '1':
            print(reverse_display(name))
        if q == '2':
            vowel_count = vowel_counter(name)
            for char, count in vowel_count.items():
                print(f'{char}: {count}')
            print(f'Total = {sum(vowel_count.values())}')   #displays the total # of vowels
        if q == '3':
            consonant_count = consonant_counter(name)
            for char, count in consonant_count.items():
                print(f'{char}: {count}')
            print(f'Total = {sum(consonant_count.values())}')   #displays the total # of consonants
        elif q == '4':
            print(first_name(name))
        elif q == '5':
            print(last_name(name))
        elif q == '6':
            print(middle_name(name))
        elif q == '7':
            print(last_hyphen_checker(name))
        elif q == '8':
            print(lower_case(name))
        elif q == '9':
            print(upper_case(name))
        elif q == '10':
            print(scramble_name(name))
        elif q == '11':
            print(palindrome_checker(name))
        elif q == '12':
            print(sort(name))
        elif q == '13':
            print(initial(name))
        elif q == '14':
            print(title_checker(name))
        elif q == 'q':
            break
        else:
            print('Please enter a corresponding number for a function or q to quit')
main()