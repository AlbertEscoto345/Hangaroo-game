secretWord = 'comet'
from firstfunction import isWordGuessed
from secondfunction import getGuessedWord
from thirdfunction import getAvailableLetters
lettersGuessed = [' ', ' ', ' ', ' ', ' ']

def InputEval(input):
    if (input == 'c'):
        lettersGuessed[0+1] = lettersGuessed[0]
        lettersGuessed[0] = 'c'
        pass
    elif (input == 'o'):
        lettersGuessed[1+1] = lettersGuessed[1]
        lettersGuessed[1] = 'o'
        pass
    elif (input == 'm'):
        lettersGuessed[2+1] = lettersGuessed[2]
        lettersGuessed[2] = 'm' 
        pass
    elif (input == 'e'):
        lettersGuessed[3+1] = lettersGuessed[3]
        lettersGuessed[3] = 'e' 
        pass
    elif (input == 't'):
        lettersGuessed[4] = 't'
        pass
    else:
        print("Not one of the remaining unknown letters; guess again!")

lettersGuessed[0] = input("Guess a letter! ")
InputEval(input)
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed)
returner = isWordGuessed(secretWord, lettersGuessed)
print(returner)

lettersGuessed[1] = input("Guess a letter! ")
InputEval(input)
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed)  
returner = isWordGuessed(secretWord, lettersGuessed)
print(returner)

lettersGuessed[2] = input("Guess a letter! ")
InputEval(input)
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed)  
returner = isWordGuessed(secretWord, lettersGuessed)
print(returner)

lettersGuessed[3] = input("Guess a letter! ") 
InputEval(input) 
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed) 
returningstring = getGuessedWord(secretWord, lettersGuessed)
print(returner)

lettersGuessed[4] = input("Guess a letter! ")
InputEval(input)        
returningstring = getGuessedWord(secretWord, lettersGuessed)
newAvailableLetters = getAvailableLetters(lettersGuessed)
returner = isWordGuessed(secretWord, lettersGuessed)
print(returner)

