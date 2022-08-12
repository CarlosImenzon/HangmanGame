"""
Module where the logic of the game 'Hangman' is found.

This class provides methods to solve the problem.
"""
import random
from categories import *

# -------------------------------------------------------------------
'''
Take a random word from the list belonging to the selected category.

Parameters:
- cat: list with all the words belonging to the selected category.

Return:
    Returns the random word.
'''
def categoryWord(cat):
    if cat==1:
        return random.choice(frutas)
    if cat==2:
        return random.choice(verduras)
    if cat==3:
        return random.choice(profesiones)
    if cat==4:
        return random.choice(colores)
    if cat==5:
        return random.choice(animales)
    if cat==6:
        return random.choice(deportes)
# -------------------------------------------------------------------
'''
Checks if the character exists in the word, counting the
amount of appearance and asking if it is greater than zero.

Parameters:
- lyrics: character that the user enters when playing. 
- word: word in play.

Return:
    Returns 'True' if the lyrics are found, else returns 'False'. 
'''
def thereIsCharacterInWord(lyrics, word):
    cont = 0
    cont += word.count(lyrics)
    if lyrics=='A' or lyrics=='E' or lyrics=='I' or lyrics=='O' or lyrics=='U':
        cont += word.count(tilde(lyrics))
    return cont>0

# -----------------------------------------------------------------
'''
Given a vowel, it returns the same letter with the tilde.

Parameters:
- lyrics: character that the user enters when playing.

Return:
    Returns the lettera with a tilde.
'''
def tilde(lyrics):
    if lyrics=='A':
        return 'Á'
    if lyrics=='E':
        return 'É'
    if lyrics=='I':
        return 'Í'
    if lyrics=='O':
        return 'Ó'
    if lyrics=='U':
        return 'Ú'
# -----------------------------------------------------------------
'''
Replace each letter of the word with '_' to start the game.

Parameters:
- word: word in play.

Return:
    Returns a list where each character was replaced by a '_',
    the list is the length of the word (one character per index).
'''
def replaceUnderscore(word):
    listPal=[]
    for i in range(0,len(word)):
        listPal.append('_')
    return listPal

# ----------------------------------------------------------------
'''
If the letter to verify belongs to the word in game, replace
the '_' in the letter in the partial result.

Parameters:
- lyrics: character that the user enters when playing.
- word: word in play.
- partialResult: list with the partial result of the game
(includes the letters guessed right so far and '_' for the missing guess).

Return:
    Returns the list with the partial result.
'''
def replaceLetter(lyrics, word, partialResult):
    cont=0
    for i in word:
        if i==lyrics:
           partialResult[cont]=i
        if i==tilde(lyrics):
               partialResult[cont]=tilde(lyrics) 
        cont+=1
    return partialResult

# ----------------------------------------------------------------
'''
Checks for '_'. Returns True if the word is complete.

Parameters:
- word: word in play.

Return:
    Checks if the user completes all the boxes of the word in game.
'''
def verifyWinner(word):
    if word.count('_') == 0:
        return True
    else:
        return False

# -------------------------------------------------------------
'''
Checks if the letter exists in those that were already entered by the user,
if it does not belong to the list, it adds it.

Parameters:
- lyrics: character that the user enters when playing.
- lyricsList: list where the letters that were already entered are stored.

Return:
    Returns 'False' if the letter is already in the list, otherwise adds it
    and returns 'True'.
'''
def listLettersEntered(lyrics, lyricsList):
    if lyrics in lyricsList:
        return False
    else:
        lyricsList.append(lyrics)
        return True

# -------------------------------------------------------------