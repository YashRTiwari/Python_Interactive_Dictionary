import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))

notFound = ["Sorry! The word doesn't exist in the dictionary"]


def getDef(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    else:
        w = get_close_matches(word, data.keys(), 1, 0.8)
        if len(w) != 0:
            check = input("Enter Y if you meant '%s', else N : " % w[0])
            if  check == 'Y':
                return data[w[0]]
            else :
                return getDef(input("Try Again!\nEnter word: "))
        else:
            return notFound

word = input("Enter word: ")
answerList = getDef(word.lower())

for answer in answerList:
    print(answer)
