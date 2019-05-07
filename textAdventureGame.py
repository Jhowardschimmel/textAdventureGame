"""
A mini text-based adventure game. Shows examples of using:
importing libraries
printing
user input
defining a function
assigning a variable
if/else statements
while loop
random numbers
"""

import time
import random

again = True
while again:
    

    #game function
    def game():
        
        #question function returns true if users inputs 'y' or 'yes'
        def ask(question):
            answer = input(question + "[y/n] \n")
            return answer in ['y', 'yes']
            
            
        name = input("What is your name? \n")
        print "Hello, " + name
        age = int(input("How old are you? \n"))
        min_age = str(age + random.randint(1,10))
        print "Oh no! You are much to young to be an adventurer. An adventurer must be at least " + min_age +" years old."
        answer = input( "Are you sure that you want to go adventuring? \n")
        if answer == "y":
            print "That's the spirit!"
        else:
            print"Okay, well that was a boring. Maybe something more interesting will happen next time."
            complete = 1
            return complete
            
                
        print "Look behind you, " + name + ". Do you see that cave?"
        if ask("Want to go spelunking?"):
            #this first answer will print when the user inputs 'y' or 'yes'
            print "Fantastic! Let's go!"
        else:
            #this answer will print if the user inputs anything else
            print "I think you meant to say yes. Fantastic! Let's go!"
        
        #this pauses the game for 1 second. For dramatic effect.       
        time.sleep(1)
        
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the cave of secrets!")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
                
        time.sleep(1)
        print "You run into a hideous bat!"
        
        
        fight = input("Do you want to fight it? [y/n] \n")
        if fight =="n":
            print"Okay, well that was a boring. Maybe something more interesting will happen next time."
            complete = 1
            return complete
        else:    
        
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("   YOU MUST ROLL ABOVE A 5 TO KILL THE BAT    ")
            print ("IF THE BAT ROLLS HIGHER THAN YOU, YOU WILL DIE")
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            
            time.sleep(2)
            roll = int(random.randint(1, 12))
            bat_roll = int(random.randint(1, 6))
            print ("you roll a " + str(roll))
            print ("the bat rolls a " + str(bat_roll))
            time.sleep(2)
            
            if bat_roll > roll:
                print ("The bat swoops down and attacks you!")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print ("                  GAME OVER                     ")
                print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                complete = 0
                return complete
            
            elif roll < 5:
                print ("You didn't do enough damage to kill the bat, but you manage to escape. \n")
            
            else:
                print ("You killed the bat!")

        print "You enter the ominous-looking cave. You wonder around stalagmites and stalactites. \n"
        
        print "You hear a roaring sound around the corner. \n"
        if ask("Wanna take a look?"):
            print"You turn the corner to see a beautiful sleeping dragon with red and golden scales."
        else:
            print"Okay, well that was a boring adventure, maybe something more interesting will happen next time."
            complete = 1
            return complete
            
        print "This dragon looks either friendly or... \n" 
        time.sleep(2)
        print "...Hungry! \n"
        
        if ask("Do you want to take a closer look?"):
            print "She opens her big eyes and smiles.\n" + "It has been so long since I have seen an adventurer! she says." 
            print "She spreads her big wings, and you hop on. You fly out of the cave and your adventures begin."
            complete = 2
            return complete
        else:
            print "Where is your sense of adventure?!\n" 
            time.sleep(2)
            print "... Oh wait, nope, that's a hungry dragon. EEP!"
            print "You are eaten alive :("
            complete = 0
            return complete
    
    """
    this is the game loop. It asks the user if they want to play again after they
    die or beat the game.
    """
    complete = game()
    if complete == 0:
        time.sleep(2)
        again = input("\n You died. Would you like to play again? [y/n] \n")
        if again == "y":
            again
        
        else:
             break            
                
    if complete == 1:
        time.sleep(2)
        again = input("\n You survived! Would you like to play again? [y/n] \n")
        if again == "y":
            again
        
        else:
             break
         
    if complete == 2:
        time.sleep(2)
        again = input("\n You are an amazing adventurer! Would you like to go on another adventure? [y/n] \n")
        if again == "y":
            again
        
        else:
             break     
