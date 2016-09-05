#!/usr/bin/env python

#====================#
# Number Guessing AI #
#====================#

# Purpose #
# This is an example in "thinking" computers.
# One AI 1 knows a number between 1-10000 provided by the user.
# AI 2 has to guess the number using a primitive form of logic- that being process of elimination.
# AI 2 asks AI 1 if a randomly guessed number is correct. If correct program exits, else AI 1 will "apologize" to AI 2 and then tell AI 2 if the correct number is higher or lower than the incorrectly guessed number.
# It works like the computer is having a conversation with itself.

# (c) Jesse Wallace (c0deous) 2015 (jesseawallace.net) #



import os, sys, time, random

# AI 1 Logic #
def ai1(guessednum):
    # Add guess to statistics #
    numbersguessed.append(guessednum)
    if int(guessednum) == correctnum: # Correct Guess Response
        print(' ')
        print('AI 1: Correct! Nicely done my friend!')
        return(True)

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

# AI 2 Logic #
def ai2():
    newguess = random.choice(numlist) # New guess
    # Userland
    print(' ')
    print('AI 2: I would like to guess... perhaps %d?' % (newguess))
    # Ask AI1
    askai = ai1(newguess)

    # Correct Guess Response #
    if askai == True:
        print(' ')
        print('AI 2: Eureka! I have found it!')
        return('Solved')
    # False, Lower Response #
    elif askai == "False, Lower":
        # Remove Incorrect Guess from Guesslist #
        if newguess in numlist:
            numlist.remove(newguess)
        else:
            raise Exception('Incorrect guess was not in numlist')

        # Remove all higher numbers #
        for i in list(range(newguess + 1, 10001)):
            if i in numlist:
                numlist.remove(i)
        return(True)
    # False, Higher Response #
    elif askai == "False, Higher":
        # Remove Incorrect Guess from Guesslist #
        if newguess in numlist:
            numlist.remove(newguess)
        else:
            raise Exception('Incorrect guess was not in numlist')

        # Remove all lower numbers #
        for i in list(range(1, newguess)):
            if i in numlist:
                numlist.remove(i)
        return(True)

def runstatistics():
    print(' ')
    print(' Statistics')
    print('------------')
    print('Times Guessed: %d' % (len(numbersguessed)))
    print('Numbers Guessed: %s' % (numbersguessed))
    print(' ')

def main():
    global timesguessed
    global numbersguessed
    global correctnum
    try:
        # Get number from user #
        correctnum = int(raw_input('Please provide a positive integer in range 1-10,000: '))
        if correctnum <= 10000 and correctnum > 0: # Validate Input
            # Tell AI2 to start Guessing
            timesguessed = 0
            numbersguessed = []
            while True:
                if ai2() == 'Solved':
                    runstatistics() # Show Statistics
                    break
        else:
            raise ValueError
    except ValueError:
        print('[-] Invalid Number: Must be a positive integer')
        main()

if __name__ == '__main__':
    # Intro Conversation #
    print('AI 1: Would you like to play a game?')
    time.sleep(2)
    print(' ')
    print('AI 2: Let us begin...')
    time.sleep(1.5)
    print('')
    raw_input(' PRESS ENTER TO BEGIN ')
    print('')

    # Init #
    numlist = list(range(1, 10001))

    main()
