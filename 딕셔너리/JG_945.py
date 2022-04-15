dic={
    "Pokemon" : "Pikachu",
    "Digimon" : "Agumon",
    "Yugioh" : "Black Magician"
}

userInput=input()
if dic.get(userInput):
    print(dic[userInput])
else:
    print("I don't know")