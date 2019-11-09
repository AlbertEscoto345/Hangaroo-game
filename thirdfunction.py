def getAvailableLetters(lettersGuessed):
    import string
    all_letters = list(string.ascii_lowercase)
    all_lettersSet = set(all_letters)
    lettersGuessedSet = set(lettersGuessed)
    newAvailableLetters = all_lettersSet.difference(lettersGuessedSet)
    print(''.join(sorted(newAvailableLetters, reverse=False)))
    return newAvailableLetters

