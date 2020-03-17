''' 
Hangman Program Attempt
With special thanks to github user erossignon for the quotes.
'''
import random
import string
import sys

def main(): #Initializes the game before playing
    prompt = input("Do you have your own text file for hangman? If not, a default will be provided. (Y/N):")
    prompt = prompt.upper()
    if prompt == "Y":
        fileName = input("Please give a filename that contains quotes enclosed in quotation marks. (Be sure to include .txt at the end): ")
        quoteList = openFile(fileName)
    else:
        quoteList = openFile()
    quoteNo = random.randint(0, len(quoteList))
    quote = quoteList[quoteNo]
    blanks = convertQuote(quote)
    playGame(quote, blanks)

def openFile(fileName = "defaultFile.txt"): #Opens the file containing a number of quotes. Note: Quotes must be enclosed in quotation marks
    try:
        file = open(fileName, "r", errors="ignore")
        file1 = file.readlines()
        quoteList = []
        for quote in file1:
            startQuote = int(quote.find("\""))
            endQuote = int(quote.rfind("\""))
            if startQuote == -1:
                continue
            completeQuote = quote[startQuote+1:endQuote]
            quoteList.append(completeQuote)
        return quoteList
    except:
        print("Please enter a valid filename. Ensure that the file is in the same directory as this program.")
        print("For the default file, type defaultFile.txt")
        fileName = input("Please give a filename that contains quotes enclosed in quotation marks. (Be sure to include .txt at the end): ")
        return openFile(fileName)

def convertQuote(quote): #Converts quote to a list, with each letter, space, and punctuation as its own element
    blanks = []
    for i in range(len(quote)):
        if (quote[i] in (string.punctuation)) or (quote[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            blanks.append(quote[i])
        elif (quote[i] == " "):
            blanks.append(" ")
        else:
            blanks.append("_")

    return blanks

def printGame(convertedQuote): #Outputs what would be written down on paper as if we were playing in real life
    wordCount = 1
    for i in range(len(convertedQuote)):
        if convertedQuote[i] == " ":
            wordCount += 1
        if wordCount % 5 == 0:
            print()
            wordCount +=1
        print(convertedQuote[i], end =" ")

def guessCheck(guess, quote, quoteList): #Checks to see if the letter exists in the quote. If not, returns False
    occurrenceCount = 0
    for i in range(len(quoteList)):
        if guess == quote[i].lower():
            quoteList[i] = guess
            occurrenceCount += 1
    if occurrenceCount:
        return quoteList
    else:
        return False

def endGame(tries, quoteList, quote): #Checks if the game is over before each guess and ends the game if win/lose occurs
    if "_" in quoteList:
        if not tries:
            print("You've run out of tries and have lost. The quote was: \n", quote)
        else:
            return False
    else:
        print("Congratulations, you've won! The quote was:", quote)
        return True

def solveCheck(quote): #Checks if the user solved correctly. If not, they lose completely.
    guess = input("What is your guess? ")
    if quote.lower() == guess.lower():
        print("You've won! The quote was:", quote)
        sys.exit()
    else:
        print("Sorry, you've lost. The quote was:", quote)
        sys.exit()

def playGame(quote, emptyQuoteList): #Plays the game
    guessedLetters = set()
    tries = 8
    quoteList = emptyQuoteList
    while tries and not endGame(tries, quoteList, quote):
        print("Current Tries:", tries, "Current guesses:", guessedLetters)
        printGame(quoteList)
        guess = input("\n Please input a guess. It may be a single digit. If you'd like to solve, type 'solve': ")
        if guess.lower() == "solve":
            solveCheck(quote)
        guessedLetters.add(guess)
        temp = guessCheck(guess, quote, quoteList)
        if not temp:
            tries -= 1
            endGame(tries, quoteList, quote)
        else:
            quoteList = temp

if __name__ =='__main__':
    main()
