+#Lara Alisha Willson
#This program greets user and has them choose a different language to greet them in.
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


if int(Lang) > 3 or int(Lang) < 1:
    print('That was not an option, silly!')
elif Lang == '1':
    print('Bonjour, mon cheri!')
elif Lang == '2':
    print('RAWWWWWRRRRR!!!!')
elif Lang == '3':  
    print('How you doing?')
            
#Here we are asking the user to exit the program. Since it is in a while loop, if the user does not enter exit, the program will complain it wants to go back to sleep and prompt the user for an answer again. 
   
import sys
    
while True:
    print('Type exit to exit.')
    answer = input()
    if answer == 'exit':
        sys.exit()
    print('Just let me go back to sleep already.')
