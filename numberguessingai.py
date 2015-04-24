#!/usr/bin/env python3

#====================#
# Number Guessing AI #
#====================#

# Purpose #
# This is an example in "thinking" computers.
# One AI 1 knows a number between 1-100 provided by the user.
# AI 2 has to guess the number using a primitive form of logic- that being process of elimination.
# AI 2 asks AI 1 if a randomly guessed number is correct. If correct program exits, else AI 1 will "apologize" to AI 2 and then tell AI 2 if the correct number is higher or lower than the incorrectly guessed number.
# It works like the computer is having a conversation with itself.

# (c) Jesse Wallace (c0deous) 2015 (jesseawallace.net) #

import os, sys, time, random


def main():
    # Intro Conversation #
    time.sleep(0.75)
    print('AI 1: Would you like to play a game?')
    time.sleep(2)
    print(' ')
    print('AI 2: Let us begin...')
    time.sleep(1.5)
    print('')
    input('PRESS ENTER TO BEGIN')
    print('')
    
    # Init Statistics #
    timesguessed = 0
    numbersguessed = []
    
    # Get number from user #
    correctnum = input('Please provide a positive integer in range 1-10,000: ')
    correctnum = int(correctnum)
    if correctnum < 10001 and correctnum > 0: # Validate input
        pass
    else:
        print('')
        print('Invalid number; Number must be in range 1-10,000')
        exit()
    
    # AI 1 Logic #
    def ai1(guessednum):
        # Add guess to statistics #
        #timesguessed = timesguessed + 1
        #numbersguessed.append(guessednum)
        if int(guessednum) == correctnum: # Correct Guess Response
            print(' ')
            print('AI 1: Correct! Nicely done my friend!')
            return(True)
            #runstatistics()
        
        else: # Incorrect Guess Response
            print(' ')
            print('AI 1: Sorry old friend! You have guessed incorrectly')
            if guessednum > correctnum: # Hint: Lower
                print(' ')
                print('(AI 1 whispers to AI 2): The number you seek appears to be lower than the number you have just guessed! Good luck my friend!')
                return('False, Lower')
            elif guessednum < correctnum: # Hint: Higher
                print(' ')
                print('(AI 1 whispers to AI2): The number you seek appears to be higher than the number you have just guessed! Good luck my friend!')
                return('False, Higher')
    
    # Numlist Init #
    numlist = list(range(1, 10001))
    
    # AI 2 Logic #
    def ai2():
        newguess = random.choice(numlist)
        print(' ')
        print('AI 2: I would like to guess... perhaps ' + str(newguess) + '?')
        askai = ai1(newguess)
        
        #print(askai)
        
        if askai == True:
            print(' ')
            print('AI 2: Eureka! I have found it!')
            return(False)
        elif askai == "False, Lower":
            print(' ')
            print('AI 2: Alas! It is so close yet so far...')
            # Remove Incorrect Guess from Guesslist #
            if newguess in numlist:
                numlist.remove(newguess)
            else:
                print(' ')
                print('AI 2: I have encountered an error in my logic! Shutting down...')
                exit()
            
            # Remove all higher numbers #
            nextnum = newguess + 1
            lowernumlist = list(range(nextnum, 10001))
            for i in lowernumlist:
                if i in numlist:
                    numlist.remove(i)
            #print(numlist)
            return(True)
                
        elif askai == "False, Higher":
            print(' ')
            print('AI 2: Alas! It is so close yet so far...')
            # Remove Incorrect Guess from Guesslist #
            if newguess in numlist:
                numlist.remove(newguess)
            else:
                print(' ')
                print('AI 2: I have encountered an error in my logic! Shutting down...')
                print(' ')
                print('AI 1: Maybe another time then... ')
                exit()
            
            # Remove all lower numbers #
            highernumlist = list(range(1, newguess))
            for i in highernumlist:
                if i in numlist:
                    numlist.remove(i)
            #print(numlist)
            return(True)
    
    def runstatistics():
        print(' Statistics')
        print('|------------|')
        print('Times Guessed: ' + int(timesguessed))
        print('Numbers Guessed: ' + str(numbersguessed))
    
    # Initialize the Sequence #
    while True:
        if not ai2():
            break
        
        
if __name__ == '__main__':
    main()