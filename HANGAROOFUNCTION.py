def Hangaroo(secretWord):
    from firstfunction import isWordGuessed
    from secondfunction import getGuessedWord
    from thirdfunction import getAvailableLetters
    lettersGuessed = [' ', ' ', ' ', ' ', ' ']
    mistakesMade = 0

    def InputEval(userinput):
        if (userinput == 'c' and lettersGuessed[0] != 'c'):
            lettersGuessed[4] = lettersGuessed[0]
            lettersGuessed[0] = 'c'
            pass
        elif (userinput == 'o' and lettersGuessed[1] != 'o'):
            lettersGuessed[4] = lettersGuessed[1]
            lettersGuessed[1] = 'o'
            pass
        elif (userinput == 'm' and lettersGuessed[2] != 'm'):
            lettersGuessed[4] = lettersGuessed[2]
            lettersGuessed[2] = 'm' 
            pass
        elif (userinput == 'e' and lettersGuessed[3] != 'e'):
            lettersGuessed[4] = lettersGuessed[3]
            lettersGuessed[3] = 'e' 
            pass
        elif (userinput == 't' and lettersGuessed[4] != 't'):
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

    lettersGuessed[0] = input("Guess a letter! (5 tries remaining!) ")
    userinput = lettersGuessed[0]
    lettersGuessed = [element.lower() for element in lettersGuessed] ; lettersGuessed
    userinput = lettersGuessed[0]
    InputEval(userinput)
    returningstring = getGuessedWord(secretWord, lettersGuessed)
    print("Available letters:")
    newAvailableLetters = getAvailableLetters(lettersGuessed)
    returner = isWordGuessed(secretWord, lettersGuessed)
    print("Is the word guessed?")
    print(returner)
    mistakesMade = MistakeCounter(mistakesMade)
    print("Wrong letters guessed (letters not part of the word):")
    print(mistakesMade)

    lettersGuessed[1] = input("Guess a letter! (4 tries remaining!) ")
    userinput = lettersGuessed[1]
    lettersGuessed = [element.lower() for element in lettersGuessed] ; lettersGuessed
    userinput = lettersGuessed[1]
    InputEval(userinput)
    returningstring = getGuessedWord(secretWord, lettersGuessed)
    print("Available letters:")
    newAvailableLetters = getAvailableLetters(lettersGuessed)  
    returner = isWordGuessed(secretWord, lettersGuessed)
    print("Is the word guessed?")
    print(returner)
    mistakesMade = MistakeCounter(mistakesMade)
    print("Wrong letters guessed (letters not part of the word):")
    print(mistakesMade)

    lettersGuessed[2] = input("Guess a letter! (3 tries remaining!) ")
    userinput = lettersGuessed[2]
    lettersGuessed = [element.lower() for element in lettersGuessed] ; lettersGuessed
    userinput = lettersGuessed[2]
    InputEval(userinput)
    returningstring = getGuessedWord(secretWord, lettersGuessed)
    print("Available letters:")
    newAvailableLetters = getAvailableLetters(lettersGuessed)  
    returner = isWordGuessed(secretWord, lettersGuessed)
    print("Is the word guessed?")
    print(returner)
    mistakesMade = MistakeCounter(mistakesMade)
    print("Wrong letters guessed (letters not part of the word):")
    print(mistakesMade)

    lettersGuessed[3] = input("Guess a letter! (2 tries remaining!) ")
    userinput = lettersGuessed[3]
    lettersGuessed = [element.lower() for element in lettersGuessed] ; lettersGuessed
    userinput = lettersGuessed[3]
    InputEval(userinput)        
    returningstring = getGuessedWord(secretWord, lettersGuessed)
    print("Available letters:")
    newAvailableLetters = getAvailableLetters(lettersGuessed)
    returner = isWordGuessed(secretWord, lettersGuessed)
    print("Is the word guessed?")
    print(returner)
    mistakesMade = MistakeCounter(mistakesMade)
    print("Wrong letters guessed (letters not part of the word):")
    print(mistakesMade)

    lettersGuessed[4] = input("Guess a letter! (1 try remaining!)")
    userinput = lettersGuessed[4]
    lettersGuessed = [element.lower() for element in lettersGuessed] ; lettersGuessed
    userinput = lettersGuessed[4]
    InputEval(userinput)        
    returningstring = getGuessedWord(secretWord, lettersGuessed)
    print("Available letters:")
    newAvailableLetters = getAvailableLetters(lettersGuessed)
    returner = isWordGuessed(secretWord, lettersGuessed)
    print("Is the word guessed?")
    print(returner)
    mistakesMade = MistakeCounter(mistakesMade)
    print("Wrong letters guessed (letters not part of the word):")
    print(mistakesMade)
    
    if(returner == True):
        print("Congratulations! You guessed the word!")
    else:
        print("Sorry! Better luck next time!")
        
    lettersGuessed = [' ', ' ', ' ', ' ', ' ']
    mistakesMade = 0