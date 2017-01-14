#HangMan
import random
wordsList = ["Swasta","Binajola","Manda","Janpachola"]
count = 0
win = 0
word = wordsList[random.randint(0,3)]
gword = list()
for i in range (0,len(word)):
    gword += "*"
checkwordlist = list()

def findthroughList(character):
    for i in checkwordlist:
        if i == character:
            return 1
    checkwordlist.append(character)
    return 0

def checkWord(character):
   # print word.find(character),word.index(character),findthroughList(character)
    indexcount = 0
    if (word.find(character)+1) and (not findthroughList(character) ):
            for i in word:
                if i == character:
                    global win
                    win += 1
                    gword[indexcount] = character[0]
            #gword[word.index(character)] = character
                indexcount += 1

            return 1
    return 0



print "LEts PLAy HANGMAN xD\n"
#3 tries
count =0
while count <= 3 and win != len(word):
    print gword
    character = raw_input("Enter the Guess\n")
    if not checkWord(character):
        count += 1
    print count,"Wrong Tries\n"
    if count == 4:
        print "You Lose"
    elif win == len(word):
        print "You Win"
