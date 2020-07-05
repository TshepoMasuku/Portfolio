import time
import random
def Story():
    print('Once apon a time,')
    time.sleep(2)
    print('There lived a kid whos math intuition was very strong.')
    time.sleep(3)
    print('Now you are given an opportunity to play a game with the kids mind built within this game.')
    time.sleep(5)

def Game():
    print('Do you wish to play the game with the kid,')
    time.sleep(2)
    print('yes or no ?')
    Play = input()
    if Play == PlayChoice[0]:
        print('okay good choice.')
        time.sleep(2)
        print('Can you guess the kid\'s first number between 0 and 9.')
        tryNUMone,tryNUMtwo = [1,1]
        tryguessum = 1
        SCORE  = 100
        NUMone,NUMtwo = [random.randint(0,9),random.randint(0,9)]
        while tryNUMone <= 5:
            GuessNUMone = input()
            GuessNUMone = int(GuessNUMone)
            tryNUMone += 1
            if NUMone==GuessNUMone:
                print('Your guess '+str(GuessNUMone)+' is correct.')
                break
            if GuessNUMone>NUMone:
                print('Your guess is higher than what the kid is thinking and you have '+str(6-tryNUMone)+' guesses left.')
                SCORE -= 5
            if GuessNUMone<NUMone:
                print('Your guess is lower than what the kid is thinking and you have '+str(6-tryNUMone)+' guesses left.')
                SCORE -= 5
            if tryNUMone == 6:
                time.sleep(2)
                print('You have ran out of your guesses.')
                
        time.sleep(2)
        print('Can you guess the kid\'s second number between 0 and 9.')

        while tryNUMtwo <= 5:
            GuessNUMtwo = input()
            GuessNUMtwo = int(GuessNUMtwo)
            tryNUMtwo += 1    
            if NUMtwo==GuessNUMtwo:
                print('Your guess '+str(GuessNUMtwo)+' is correct.')
                break
            if GuessNUMone>NUMtwo:
                print('Your guess is higher than what the kid is thinking and you have '+str(6-tryNUMtwo)+' guesses left.')
                SCORE -= 5
            if GuessNUMone<NUMtwo:
                print('Your guess is lower than what the kid is thinking and you have '+str(6-tryNUMtwo)+' guesses left.')
                SCORE -= 5
            if tryNUMtwo == 6:        
                time.sleep(2)
                print('You have ran out of your guesses.')
                    
        time.sleep(2)     
        print('What is the sum of the numbers the kid was thinking of? \nHint: The sum is between 0 and 18.')
        KidSum = NUMone+NUMtwo
        
        while tryguessum <= 2:
            guessum = input()
            guessum = int(guessum)
            tryguessum += 1
            if KidSum == guessum:
                print('Your answer is correct.')
                break
            else:
                print('Your answer is incorrect and you have '+str(3-tryguessum)+' guess left.')
                SCORE -= 25
            if tryguessum == 3:
                time.sleep(2)
                print('You have ran out of your guesses.')
                    
        print('The sum which the kid was thinking of,was '+str(KidSum)+' and your score is '+str(SCORE)+'% .')
    else:
        print('okay goodbye and have a good day.')

def GameAgain():
    print('okay good choice.')
    time.sleep(2)
    print('Can you guess the kid\'s first number between 0 and 9.')
    tryNUMone,tryNUMtwo = [1,1]
    tryguessum = 0
    SCORE  = 100
    NUMone,NUMtwo = [random.randint(0,9),random.randint(0,9)]
    while tryNUMone <= 5:
        GuessNUMone = input()
        GuessNUMone = int(GuessNUMone)
        tryNUMone += 1
        if NUMone==GuessNUMone:
            print('Your guess '+str(GuessNUMone)+' is correct.')
            break
        if GuessNUMone>NUMone:
            print('Your guess is higher than what the kid is thinking and you have '+str(6-tryNUMone)+' guesses left.')
            Score -= 5
        if GuessNUMone<NUMone:
            print('Your guess is lower than what the kid is thinking and you have '+str(6-tryNUMone)+' guesses left.')
            SCORE -= 5
        if tryNUMone == 6:
            time.sleep(2)
            print('You have ran out of your guesses.')
            
    time.sleep(2)
    print('Can you guess the kid\'s second number between 0 and 9.')

    while tryNUMtwo <= 5:
        GuessNUMtwo = input()
        GuessNUMtwo = int(GuessNUMtwo)
        tryNUMtwo += 1    
        if NUMtwo==GuessNUMtwo:
            print('Your guess '+str(GuessNUMtwo)+' is correct.')
            break
        if GuessNUMone>NUMtwo:
            print('Your guess is higher than what the kid is thinking and you have '+str(6-tryNUMtwo)+' guesses left.')
            SCORE -= 5
        if GuessNUMone<NUMtwo:
            print('Your guess is lower than what the kid is thinking and you have '+str(6-tryNUMtwo)+' guesses left.')
            SCORE -= 5
        if tryNUMtwo == 6:         
            time.sleep(2)
            print('You have ran out of your guesses.')
            
    time.sleep(2)     
    print('What is the sum of the numbers the kid was thinking of? \nHint: The sum is between 0 and 18')
    KidSum = NUMone+NUMtwo
    
    while tryguessum <= 2:
        guessum = input()
        guessum = int(guessum)
        tryguessum += 1
        if KidSum == guessum:
            print('Your answer is correct.')
            break
        else:
            print('Your answer is incorrect and you have '+str(3-tryguessum)+' guesses left.')
            SCORE -= 25
        if tryguessum == 3:
            time.sleep(2)
            print('You have ran out of your guesses.')
                
    print('The sum which the kid was thinking of,was '+str(KidSum)+' and your score is '+str(SCORE)+'% .')

Story()
PlayChoice = ['yes','no']
Game()
time.sleep(2)
print('GAME OVER!')
time.sleep(2)
print('Do you wish to play again?')
PlayAgain = input()
while PlayAgain == PlayChoice[0]:
    GameAgain()
    time.sleep(2)
    print('GAME OVER!')
    time.sleep(2)
    print('Do you want to play this game again?')
    PlayAgain = input()
    
time.sleep(1)
print('....................\t....................\t..................\n....................\t....................\t..................')    
