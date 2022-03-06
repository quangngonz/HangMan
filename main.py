import os, requests
from hangMans import hangMans

stage = 0

def getWord():
    """
    Gets a random word from the api
    [
        {
        "word": "",
        "definition": "",
        "pronunciation": ""
        }
    ]
    """
    url = "https://random-words-api.vercel.app/word"
    r = requests.get(url).json()
    return r, r[0]["word"].upper()

def GenerateWordString():
    """
    Generates a string of the word with the guessed letters
    """
    wordString = ""
    for letter in word:
        if letter in guessed:
            wordString += " " + str(letter).capitalize() + " "
        else:
            wordString += "___ "
    return wordString

def Clearterminal():
    """
    Clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def writeWord():
    """
    Writes the word to a file
    """
    with open("word.txt", "w") as f:
        f.write(str(wordFull))
        f.close()

def NewGame():
    """
    Starts a new game
    """
    global stage
    global word, wordFull
    global hangMan
    global guessed
    global lives
    global wordString

    wordFull, word = getWord()
    # word = "GART"

    # write word to file
    writeWord()

    stage = 0
    guessed = []
    hangMan = hangMans
    wordString = GenerateWordString()
    print(wordString)
    print(hangMan[stage])

NewGame()

while True:
    letter = input("Guess a letter: ").capitalize()

    if letter in word:
        guessed.append(letter)
        wordString = GenerateWordString()
        Clearterminal()
        print("Word: " , wordString)
        print(hangMan[stage])
    else:
        stage += 1
        if stage == len(hangMans)-1:
            print(hangMans[stage])
            print("The word was:" , wordFull[0]["word"])
            print("Definiton: " , wordFull[0]["definition"])
            print("Pronunciation: " , wordFull[0]["pronunciation"])
            print("You lost!")
            break

        Clearterminal()
        print(word)

        print("Word: " , wordString)
        print(stage)
        print(hangMan[stage])
        wordString = GenerateWordString()

    if "_" not in wordString:
        Clearterminal()
        print("The word was:" , word)
        print("You won!")
        break
