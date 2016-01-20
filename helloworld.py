#Lara Alisha Willson
#This program greets user and has them choose a different language to greet them in.
#I chose to use a loop to make sure the user was prompted for a value until they selected a valid option.

while True:

#Here we are acknowledging the user and asking them how they would like to be greeted.    

    print('Well, hello there!')
    print('You look mighty cultured. What language would you like me to greet you in?')

#Here are the options for the user to select from.
    
    print('1. French')
    print('2. Dinosaur')
    print('3. Sarcasm')

#Here we are defining the variable Lang as the user's response.
    
    Lang=input()

#We are using if and elif clauses to translate the response into either a greeting in their chosen language or looping the user back to the question if they do not use a valid option.
#We use the continue and break statements to send the user back to the original greeting or to end the loop if they properly choose a language.
#In order for our if clause to appropriately loop the user back, we do have to use the interger function to get the interger value of the string entered by the user. That way if the response is not between 1-3 they are prompted again. 
    
    if int(Lang) > 3 or int(Lang) < 1:
        continue
    elif Lang == '1':
        print('Bonjour, mon cheri!')
        break
    elif Lang == '2':
        print('RAWWWWWRRRRR!!!!')
        break
    elif Lang == '3':
        print('How you doing?')
        break

#The program automatically exits once it reaches the end of the instructions, otherwise, we could use exit() to close the window we were using.

    

