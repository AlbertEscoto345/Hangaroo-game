secretWord = 'comet'
from firstfunction import isWordGuessed
from secondfunction import getGuessedWord
from thirdfunction import getAvailableLetters
lettersGuessed = [' ', ' ', ' ', ' ', ' ']
mistakesMade = 0

def InputEval(userinput):
    if (userinput == 'c'):
        lettersGuessed[0+1] = lettersGuessed[0]
        lettersGuessed[0] = 'c'
        pass
    elif (userinput == 'o'):
        lettersGuessed[1+1] = lettersGuessed[1]
        lettersGuessed[1] = 'o'
        pass
    elif (userinput == 'm'):
        lettersGuessed[2+1] = lettersGuessed[2]
        lettersGuessed[2] = 'm' 
        pass
    elif (userinput == 'e'):
        lettersGuessed[3+1] = lettersGuessed[3]
        lettersGuessed[3] = 'e' 
        pass
    elif (userinput == 't'):
        lettersGuessed[4] = 't'
        pass
    else:
        print("Not one of the remaining unknown letters; guess again!")
        
def MistakeCounter(mistakesMade):
    if (userinput == 'c' or userinput == 'o' or userinput == 'm' or userinput == 'e' or userinput == 't'):
        pass
    else:
        mistakesMade += 1
    return mistakesMade

lettersGuessed[0] = input("Guess a letter! ")
userinput = lettersGuessed[0]
InputEval(userinput)
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed)
returner = isWordGuessed(secretWord, lettersGuessed)
print(returner)
mistakesMade = MistakeCounter(mistakesMade)
print(mistakesMade)

lettersGuessed[1] = input("Guess a letter! ")
userinput = lettersGuessed[1]
InputEval(userinput)
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed)  
returner = isWordGuessed(secretWord, lettersGuessed)
print(returner)
mistakesMade = MistakeCounter(mistakesMade)
print(mistakesMade)

lettersGuessed[2] = input("Guess a letter! ")
userinput = lettersGuessed[2]
InputEval(userinput)
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed)  
returner = isWordGuessed(secretWord, lettersGuessed)
print(returner)
mistakesMade = MistakeCounter(mistakesMade)
print(mistakesMade)

lettersGuessed[3] = input("Guess a letter! ") 
userinput = lettersGuessed[3]
InputEval(userinput) 
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed) 
returningstring = getGuessedWord(secretWord, lettersGuessed)
print(returner)
mistakesMade = MistakeCounter(mistakesMade)
print(mistakesMade)

lettersGuessed[4] = input("Guess a letter! ")
userinput = lettersGuessed[4]
InputEval(userinput)        
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed)
returner = isWordGuessed(secretWord, lettersGuessed)
print(returner)
mistakesMade = MistakeCounter(mistakesMade)
print(mistakesMade)

