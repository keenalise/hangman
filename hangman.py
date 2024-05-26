import random
from yoo import words


#------------ For a random word generator-----------
def random_word():
    word= random.choice(words)
    return word.lower()


def game(word):
    word_complete = "*" * len (word)
    guess = False
    guessedletterlist = [] # to store the letter that user input
    guessedwordlist= [] # to store the word that is found
    
    tries = 6 #number of tries (head, body, hands*2, legs*2)
    
    
    print("yeah Yooooo!")
   
    print("Welcome to the hangman game!")
    print(failedtries(tries))
    
    
    print(word_complete)
    
    while (not guess and tries>0):
        guessletter = input("Guess any letter:").lower()
        
        if len(guessletter) ==1 and guessletter.isalpha():
            # string should be one and it should be an alphabet
            if guessletter in word: #check if the letter is in the word
                print("congratulations!!! ")
                print("\n")
                print(f"{guessletter} is in the word")
                word_in_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter==guessletter]
                for index in indices:
                    word_in_list[index] = guessletter
                    
                    
                word_in_list = "".join(word_in_list) 
                if "*" not in word_complete:
                    guess = True   
                    
                
                guessedletterlist.append(guessletter) #store the letter that user guessed
                
                
         
            elif guessletter in guessedletterlist: 
                # if the word is already guessed and is append in the guessletterlist
                print(f"Youy have already guessed the letter {guessletter}")
                
                
            else:# check if it is in the word 
                print(f" {guessletter} is not in word.")
                tries -= 1
                guessedletterlist.append(guessletter)
                print(guessedletterlist)
            
            
        
        
        else:
            print("not a valid guess")
            
        print(failedtries(tries))
        print(word_complete)
        
        if guess==word:
            print("congratulations you win.")
            
        else: 
            print(f" sorry better luck next time. {word} was teh correct time.")
            
           
def failedtries(tries): 
    attempts= [ 
               
    r'''
           
                    ----------
                    |       |
                    |       O
                    |     \ | /
                    |       |
                    |       |
                    -      / \
    
    
    
    ''',
    
    '''
           
                    ----------
                    |       |
                    |       O
                    |     \ | /
                    |       |
                    |       |
                    -      /
    
    
    
    ''',
    #fifth failed guess
    
    '''
    
                    ----------
                    |       |
                    |       O
                    |     \ | /
                    |       |
                    |       |
                    -
    
    
    
    ''', 
    #fourth failed guess
    
    '''
    
                    ----------
                    |       |
                    |       O
                    |     \ | 
                    |       |
                    |       |
                    -
    
    
    
    ''', 
    #third failed guess
    
    
    '''
        
                    ----------
                    |       |
                    |       O
                    |       | 
                    |       |
                    |       |
                    -
    
    
    ''', 
    #second failed guess
    
    
    '''
        
                          
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                   
                      
    
    
    
    ''', 
    #first failed guess
    
    
    
    
    
       '''
              
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                   
                    
                      
    
    '''
    #initial diagram
     ]
    return attempts[tries]
                      
                
            
         

def main2():
    word= random_word()
    game(word)
    word = random_word()
    game(word)
    


main2()
    
    
    


