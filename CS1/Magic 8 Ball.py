import random       

while True:                                                          #forever loop
    magic = ['Yes', 'No', 'Maybe', 'Ask again later']                #create list magic with items 'Yes', 'No', 'Maybe' 'Ask again later'
    question = input('Ask a question')                               #prompt user to ask a question
    
    if not question.endswith('?'):
        print('Please ask a question')
        continue

    response = random.choice(magic)                                  #set response to a random item from magic list
    print(response)                                                  #display response
    
    playagain = input('Do you want to ask a question?').lower()      #prompt user to answer question, convert to lowercase
    
    if playagain == "no":                                            #if user responds no
        print('Thanks for playing')                                  #display message
        break                                                        #end forever loop
    