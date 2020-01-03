import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import os 
dir_path = os.path.dirname(os.path.realpath("data.json"))
data = json.load(open(dir_path.replace("/code","/data")+"/data.json"))

def get_the_meaning(word):
    if word in data:
        return data[word]
    else:
        #matches = get_close_matches(word,data.keys())
        matches = get_close_matches(word,data.keys(),cutoff= 0.8) #The number 0.8 gives soe
        if len(matches) >0:
            if matches[0] in data:
                found_word = matches[0]
                matched_word = data[found_word]
                answer = input("Did  you mean "+ found_word+ " instead?" +" Please enter Y or N ")
                if str.lower(str.strip(answer)) == 'n':
                    return "The word doesn't exist . Please double check it"
                elif str.lower(str.strip(answer)) == 'y':
                    return matched_word
                else:
                    print("Invalid input")
            else:
                return "The word doesn't exist . Please double check it" 
        else:
            return "The word doesn't exist . Please double check it"


while True:
    entered_word = input("Enter the word to find it's meaning . Enter /exit to exit  the application.   ")
    if entered_word == "/exit":
        print("Exiting application")
        exit()
    else:
        return_value = get_the_meaning(entered_word.lower())
        if return_value == "The word doesn't exist . Please double check it": 
            print(return_value)
        else:
            if isinstance(return_value[0],list):
                print("Meaning is :","\n")
                for item in return_value[0]:
                    print(item)
            elif isinstance(return_value[0],str):
                print("Meaning is :", return_value[0])
    