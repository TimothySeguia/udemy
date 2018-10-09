import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json","r"))
# print(data)
# data is a dictionary
# print(data.keys())
# print(data["rain"])


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no:  " % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "This word doesn't exist, please try again."
        else:
            return "We didn't understand your entry"
    else:
        return "This word doesn't exist, please check it again."

    '''
    for words in data.keys():
        while words.upper() != w.upper():
            
        if words.upper() == w.upper():
            # print(words.upper() + "\n")
            # print(w.upper() + "\n")
            return data[words]
        else:
            return "This word doesn't exist, try again."
    '''


userInput = input("What word would you like to look up? ")
# print(translate(userInput))
if type(translate(userInput)) == list:
    for i in translate(userInput):
        print(" + " + i + "\n")
else:
    print(translate(userInput))
# print(SequenceMatcher(None, "rainn","rain").ratio())
# print(get_close_matches("rainn", ["help", "rain", "pyramid"]))

