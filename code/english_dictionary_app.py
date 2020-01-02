import json
data = json.load(open("/Users/tejasdongre/Tejas/Personal/Python/Interactive_English_Dictionary/An-Interactive-English-Dictionary/data/data.json"))

def get_the_meaning(word):
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist . Please double check it"


while True:
    entered_word = input("Enter the word for meaning ")
    if entered_word == "/exit":
        print("Exiting application")
        exit()
    else:
        return_value = get_the_meaning(entered_word.lower())
        if "return_value" == "The word doesn't exist . Please double check it": 
            print(return_value)
        else:
            print("Meaning is :", get_the_meaning(str.lower(entered_word)))
    