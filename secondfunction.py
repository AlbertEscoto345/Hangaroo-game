def getGuessedWord(secretWord, lettersGuessed):
    if(lettersGuessed[1] == ' ' and lettersGuessed[2] == ' ' and lettersGuessed[3] == ' '):
        global returningstringOLD
        returningstring = ['_', '_', '_', '_', '_']
        returningstringOLD = []
    else:
        returningstring = returningstringOLD
        
    if(lettersGuessed[0] == 'c'):
            returningstring[0] = 'c'
    else:
           pass
    if(lettersGuessed[1] == 'o'):
            returningstring[1] = 'o'
    else:
           pass
    if(lettersGuessed[2] == 'm'):
            returningstring[2] = 'm'
    else:
           pass
    if(lettersGuessed[3] == 'e'):
            returningstring[3] = 'e'
    else:
           pass
    if(lettersGuessed[4] == 't'):
            returningstring[4] = 't'
    else:
           pass 
    
    returningstringOLD = returningstring
    print (''.join(returningstring))
    return returningstring          