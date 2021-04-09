# Morse Alphabet
morse = {"*-" : "a", "-***" : "b",
         "-*-*" : "c", "-**" : "d",
         "*" : "e", "**-*" : "f",
         "--*" : "g", "****" : "h",
         "**" : "i", "*---" : "j",
         "-*-" : "k", "*-**" : "l",
         "--" : "m", "-*" : "n",
         "---" : "o", "*--*" : "p",
         "--*-" : "q", "*-*" : "r",
         "***" : "s", "-" : "t",
         "**-" : "u", "***-" : "v",
         "*--" : "w", "-**-" : "x",
         "-*--" : "y", "--**" : "z"}
morsepassword = "* *-* - **- --* *-* **- *-**"
wordtopass = "hi how are you"
def morsepass(morsepassword):
    listepass = morsepassword.split()
    result = ""
    for i in listepass:
        if i in morse:
            result += morse[i]
    print(result)
def wordtomorse(wordtopass):
    result = ""
    key_list = list(morse.keys())
    val_list = list(morse.values())
    for i in wordtopass:
        if i in morse.values():
            pos = val_list.index(i)
            result += key_list[pos] + " , "
        else:
            result += " / "

    print(result)
morsepass(morsepassword)
wordtomorse(wordtopass)