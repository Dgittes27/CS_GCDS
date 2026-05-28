import csv
import random
import string #import random

def add_entry(websites,usernames,passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords 
    '''
    website_entry = input('Enter website: ')   #Prompt user for a website
    username_entry = input('Enter username: ') #Prompt user for a username
    password_entry = input('Enter password: ') #Prompt user for a password
    websites.append(website_entry)             #Add website to websites
    usernames.append(username_entry)           #Add username to usernames
    passwords.append(password_entry)           #Add password to passwords


def change_entry(websites,usernames,passwords):
    '''
    Changes the username and password for the website the user requests.
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of usernames
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords 
    '''
    website_change = input('For which website would you like to change the information: ') #ask which website info they want to change
    
    if website_change in websites:
        web_index = websites.index(website_change) #get the index of website_change in websites
        usernames[web_index] = input('username: ') #use index of website to change the corresponding username
        passwords[web_index] = input('password: ') #use index of website to change the corresponding password
    else:
        print(f'{website_change} not in the list')


def complex_password_create():
    '''
    Generates a complex password.
    Args:
        None
    Returns:
        password (str): a complex password with integers, characters, and special characters
    '''
    while True:                
        characters = input('How many characters would you like your password to be? ')
        
        try: #checks if characters is an integer
            characters = int(characters)
            break
        except ValueError:
            print('Enter an integer')
    password_generated = [] 

    #determine how many of each type of character to use based on the given length of characters
    if characters % 4 == 0: 
        l_letters = characters//4
        u_letters = characters//4
        numbers = characters//4
        special = characters//4
    elif characters % 4 == 1:
        l_letters = 1 + characters//4 
        u_letters = characters//4
        numbers = characters//4
        special = characters//4
    elif characters % 4 == 2: 
        l_letters = 1 + characters//4 
        u_letters = 1 + characters//4
        numbers = characters//4
        special = characters//4
    elif characters % 4 == 3:
        l_letters = 1 + characters//4 
        u_letters = 1 + characters//4
        numbers = 1 + characters//4
        special = characters//4
    elif characters % 4 == 4:
        l_letters = 1 + characters//4 
        u_letters = 1 + characters//4
        numbers = 1 + characters//4
        special = 1 + characters//4

    #randomly select the calculated number of each characters to the password list
    for i in range(l_letters): 
        password_generated.append(random.choice(string.ascii_lowercase))
    for i in range(u_letters):
        password_generated.append(random.choice(string.ascii_uppercase))
    for i in range(numbers):
        password_generated.append(random.choice(string.digits))
    for i in range(special):
        password_generated.append(random.choice(string.punctuation))
    random.shuffle(password_generated) #randomly scrambles the order of the password
    return ''.join(password_generated) #return the password as a string not a list


def security_check(websites, passwords):
    '''
    Checks the security of a password, and returns a rating
    Args: 
        passwords (list): the list of passwords
        websites (list): the list websites 
    Return:
        rating (int): the rating of the password desired to be checked
    '''
    website = input('Which website would you like to check the security for: ') #prompt user to enter website they would like to check the password for
    
    if website in websites:
        web_index = websites.index(website) #check the password for that website
        password_checked = passwords[web_index]
        password_rating = 0                 #set password rating to 0
           
        if len(password_checked) > 5: 
            password_rating += 1            #if password is > 5 characters add 1 to rating
        if len(password_checked) > 8:
            password_rating += 1            #if password is > 8 characters add 1 to rating
        if len(password_checked) > 10:
            password_rating += 1            #if password is > 10 characters add 1 to rating
                
        if any(char.islower() for char in password_checked): #if any character in the password is lowercase 
            password_rating += 1
        if any(char.isupper() for char in password_checked): #if any character in the password is uppercase
            password_rating += 1
        if any(char.isdigit() for char in password_checked): #if any character in the password is a number
            password_rating += 1
        if any(char in string.punctuation for char in password_checked): #if any character in the password is a special character
            password_rating += 1
        return password_rating  
    else:
        print(f'{website} is not in the list')

def export_file(websites, usernames, passwords):
    '''
    Exports all entries entered previously into an excel file. 

    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords 
    '''
    data = zip(websites, usernames, passwords)                                 #create tuples that represent a single row in a spreadsheet from these three lists
    
    with open('pswd.csv', 'w', encoding='ISO-8859-1', newline='') as csv_file: #create a excel file and set it to writing mode
        writer = csv.writer(csv_file)                                          #create a tool to write with
        writer.writerow(['App', 'Username', 'Password'])                       #make the three rows App, Username and Password
        writer.writerows(data)                                                 #put the data from the combined lists into the excel sheet
    print('Data saved to pswd.csv')

def main():
    websites = [] #create an empty list for website
    usernames = []#create an empty list username
    passwords = []#create an empty list for password
    
    add_entry(websites, usernames, passwords)

    while True:
        choice = input('''Select an option from the table (type the number of that option or enter "q" to quit)
option 1: See all entries
option 2: Access specific entry
option 3: Add more entry
option 4: Change an entry
option 5: Generate password
option 6: Check password security
option 7: Export entry
        ''')

        if choice.lower() == 'q':
            break
        elif choice == '1':  
            for website in websites:
                print(f'website: {website}\n username: {usernames[websites.index(website)]}\n password: {passwords[websites.index(website)]}') 
        elif choice == '2':  
            website_info = input('For which website would you like to view your information: ')   
            if website_info in websites:
                print(f'website: {website_info}\n username: {usernames[websites.index(website_info)]}\n password: {passwords[websites.index(website_info)]}') 
            else:
                print(f'{website_info} is not saved')
        elif choice == '3':  
            add_entry(websites,usernames,passwords)
        elif choice == '4': 
            change_entry(websites,usernames,passwords)
        elif choice == '5':
            password_generated = complex_password_create()
            print(f'Your password is: {password_generated}')
            password_use = input('Would you like to add this password to a previously entered website or add a new entry? (for a new entry enter add, to change an entry enter change)')   
            if password_use == 'add':
                add_entry(websites,usernames,passwords)
            elif password_use == 'change':
                change_entry(websites,usernames,passwords)
        elif choice == '6':
            sec = security_check(websites, passwords)
            print(f'Your rating on a scale from 1-7 is {sec}')
        elif choice == '7':
            export_file(websites, usernames, passwords)
        else:
            print('Invalid response')
     

main()