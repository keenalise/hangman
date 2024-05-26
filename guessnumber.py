import random
num=random.randint(1,20)
guess= None


while guess!=num:
    
        guess= int ( input ("guess the number"))
        if guess.isdigit():
            guess= int (guess)
            if guess==num:
                
                print("you guesses the correct number which is {}".format(guess))
                
                break
        
        
            
            else:
                print("try again biiiiitch...")
                
        else:
            print("enter the valid number biiiiitch...")
        