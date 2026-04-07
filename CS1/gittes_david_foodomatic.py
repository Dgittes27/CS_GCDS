""""
┌───────────────────────────────────────────────────────────────────────────┐
│                            Food-o-Matic                                   │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: David Gittes                                                        │
| Course: CS1                                                               |
| Date: April 2nd, 2026                                                     |
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description:  A menu generator written in Python. The system implements   |
|   parallel arrays and for loops to randomly generate a menu, and find     |
|   the correlated price.                                                   |
|  Challenges: Generate and add the cost of flairs, calculate the total cost| 
|    for all items, ensure that the user is entering a valid number when    |
|    asking for menu items, remove the possibility of duplicate items,      |
|    don't allow the user to enter too many items, and lets the user know   |
|    if all of the menu combinations have been displayed                    |
└───────────────────────────────────────────────────────────────────────────┘
"""
import random
mains = ['cauliflower', 'tilapia fillet', 'pork loin', 'salmon', 'potatoes', 'three color squash', 'eggplant', 'steak', 'baguette']   #create a list named magic with items 'cauliflower', 'tilapia fillet', 'pork loin', 'salmon', 'potatoes', 'three color squash', 'eggplant', 'steak', 'baguette'
mains_cost = [20, 25, 28, 30, 18, 20, 22, 30, 20]  #create a list named mains_cost with items 20, 25, 28, 30, 18, 20, 22, 30, 20
flairs = ['with balsamico', 'with garlic and olive oil', 'with minted yogurt', 'with chutney', 'salad', 'with salsa', 'over sticky rice', 'au jus', 'with bashanti rice']   #create a list named flairs with items 'with balsamico', 'with garlic and olive oil', 'with minted yogurt', 'with chutney', 'salad', 'with salsa', 'over sticky rice', 'au jus', 'with bashanti rice'
flairs_cost = [1.50, 1.50, 3.50, 3.50, 6, 3.50, 5.50, 2, 5] #create a list named flairs_cost with items 1.50, 1.50, 3.50, 3.50, 6, 3.50, 5.50, 2, 5
used = [] #create an empty list for the main+flair combos that are used

while True:    #forever loop   
    order_cost = 0 #set the order cost to zero
    if len(used) == 81:        #if the length of the list used has 81 elements 
                print('All of the menu options have been displayed')     #display message
                break      #end loop
    try:                #attempt the following code
        question = int(input('How many menu items do you need?'))    #prompt user to answer "How many menu items do you need?"
    except ValueError:        #if there is an error
        continue              #go back

    if question > 81:        #if user's answer to the previous question is greater than 81
        print ('Sorry, we only have 9 menu items to choose from. Please enter a number between 1 and 81.')     #display message
        continue    #go back
    if question > 81 - len(used):        #if the length of the list used has 81 elements 
        print('You have asked for more menu items than we have (total items is 81)')     #display message
        continue     #go back
    for i in range(question):                #for every item requested by user run code   
        while True:                          #forever loop
            main = random.choice(mains)          #main is a random choice from the list of mains
            flair = random.choice(flairs)        #flair is a random choice from the list of flairs

            if main+flair in used:  #if the main+flair combo has already been used
                continue            #go back
            else:                   #otherwise
                used.append(main+flair)  #add the main+flair combo to the used list
                break               #end loop
                                             
        main_cost = mains_cost[mains.index(main)]  #get the index from the chosen mains from the list of mains, and then use the index from the mains cost to generate mains price
        flair_cost = flairs_cost[flairs.index(flair)] #get the index from the chosen flairs from the list of flairs and then use the index from the flairs cost to generate the flair's price
        item_price = main_cost + flair_cost  #the price of the item is equal to the cost of the main plus the cost of the flair
        print (f'{main} {flair}, ${item_price}') #display the main and the flair, and then display the price of the item
        order_cost += item_price #increase the price of the order by the price of the listed item
            
    print (f'\nThe cost of this order would be ${order_cost}') #display the order cost 

    while True:
        run_again = input('\nWould you like another menu? y/n: ').lower()  #prompt the user if they want another menu
        if run_again == 'n':  #if they answer no
            exit()  #terminate the code
        elif run_again == 'y': #if they answer yes
            break      #end loop
        else:          #otherwise
            print('Please answer with y or n')  #display message
            continue #go back