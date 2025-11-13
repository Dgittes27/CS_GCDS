 import time
import datetime

def print_colored_text(text, color_name):
    """
    Print the given text in a specified color.
    
    Args:
        text (str): The text to be printed.
        color_name (str): The color of the text to be printed.
    """
    
    colors = {                  # Dictionary mapping color names to their ANSI escape codes for terminal text coloring
        'black': '\033[30m',    # Black text color
        'red': '\033[31m',      # Red text color
        'green': '\033[32m',    # Green text color
        'yellow': '\033[33m',   # Yellow text color
        'blue': '\033[34m',     # Blue text color
        'magenta': '\033[35m',  # Magenta (purple) text color
        'cyan': '\033[36m',     # Cyan text color
        'white': '\033[37m',    # White text color
        'reset': '\033[0m',     # Reset text color to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m') # Get the ANSI color code for the given color name, defaulting to white if the color is not found
    print(f"{color_code}{text}\033[0m")                     # Print the text with the specified color, followed by the reset code to ensure no color leaks

current_time = datetime.datetime(2025, 10, 27, 6, 30, 0)    #set the current time to 6:30
print(current_time.strftime("%H:%M:%S"))                    #display the current time 
print_colored_text("ALARM!", "red")                         #display message "ALARM!" in red

while True:                                                 #forever loop
    snooze = input("snooze?").lower()                       #prompt user for response to snooze, convert to lowercase and store in variable

    if snooze == "yes":                                                        #if user snoozes 
        print_colored_text("go back to sleep for 5 mins", "blue")              #display message
        time.sleep(2)                                                          #pause program for 2 seconds
        current_time += datetime.timedelta(minutes=5)                          #add 5 minutes to the current time
    elif snooze == "no":                                                       #if user does not snooze
        print_colored_text ("get up", "cyan")                                  #display message in cyan
        current_time += datetime.timedelta(minutes=1)                          #add 1 minute to the current time
        break                                                                  #end forever loop
    else:                                                                      #if user responds anything else
        print_colored_text ("Please answer with yes or no", "magenta")         #display message in magenta

print(current_time.strftime("%H:%M:%S"))                                       #display current time

while True:                                                                 #forever loop
    hungry = input("Are you hungry?").lower()                               #prompt user for response to Are you hungry?, convert to lowercase and store in variable

    if hungry == "yes":                                                     #if user responds yes 
        print_colored_text("Eat a Banana", "yellow")                        #display message in yellow
        current_time += datetime.timedelta(minutes=5)                       #add 5 minutes to the current time
    elif hungry == "no":                                                    #if user responds no
        break                                                               #end forever loop
    else:                                                                   #if user responds anything else
        print_colored_text("Please answer with yes or no", "magenta")       #display message in magenta
print(current_time.strftime("%H:%M:%S"))                                    #display current time

while True:                                                                 #forever loop
    shower = input("Did you shower last night?").lower()                    #prompt user for response to Did you shower last night?, convert to lowercase and store in variable

    if shower == "yes":                                                     #if user responds yes
        print_colored_text("Make your bed", "cyan")                         #display message in cyan
        current_time += datetime.timedelta(minutes=2)                       #add 2 minutes to the current time
        break                                                               #end forever loop
    elif shower == "no":                                                    #if user responds no
        current_time += datetime.timedelta(minutes=10)                      #add 10 minutes to the current time
        print_colored_text("Shower", "cyan")                                #display message in cyan
        print(current_time.strftime("%H:%M:%S"))                            #display current time
        print_colored_text("Make your bed", "cyan")                         #display message in cyan
        current_time += datetime.timedelta(minutes=2)                       #add 2 minutes to the current time
        break                                                               #end forever loop
    else:                                                                   #if user responds anything else
        print_colored_text("Please answer with yes or no", "magenta")       #display message in magenta
        
print(current_time.strftime("%H:%M:%S"))                                    #display current time 
print_colored_text("Brush your teeth", "cyan")                              #display message in cyan
current_time += datetime.timedelta(minutes=2)                               #add 2 minutes to the current time
print(current_time.strftime("%H:%M:%S"))                                    #display current time

while True:                                                                 #forever loop
    cold = input("Is it cold outside?").lower()                             #prompt user for response to Is it cold outside?, convert to lowercase and store in variable

    if cold == "yes":                                                       #if user responds yes
        print_colored_text("Put on a shirt and a hoodie", "cyan")           #display message in cyan
        current_time += datetime.timedelta(minutes=2)                       #add 2 minutes to the current time
        break                                                               #end forever loop
    elif cold == "no":                                                      #if user responds no
        print_colored_text("Put on a shirt", "cyan")                        #display message in cyan
        current_time += datetime.timedelta(minutes=1)                       #add 1 minute to the current time
        break                                                               #end forever loop
    else:                                                                   #if user responds anything else
        print_colored_text("Please answer with yes or no", "magenta")       #display message in magenta
print(current_time.strftime("%H:%M:%S"))                                    #display current time
while True:                                                                 #forever loop
    gas = input("Does your car have gas?").lower()                          #prompt user for response to Does your car have gas?, convert to lowercase and store in variable

    if gas == "yes":                                                        #if user responds yes
        print_colored_text("Drive to work", "red")                          #display message in red
        break                                                               #end forever loop
    elif gas == ("no"):                                                     #if user responds no
        print_colored_text("Walk to work", "green")                         #display message in green
        break                                                               #end forever loop
    else:                                                                   #if user responds anything else 
        print_colored_text("Please answer with yes or no", "magenta")       #display message in magenta

