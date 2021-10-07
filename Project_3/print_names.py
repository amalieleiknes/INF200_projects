# function that takes in a file and reads it. It prints out the names in a sentence, but max 2 names per line.
""" kan prøve å fjerne tegnsetting og endre på formatet om det er 0 eller 1 navn, i tillegg til å
legge til muligheten for å printe ut flere navn.
"""


def printFromList(fileName):
    word1 = ""
    word2 = ""
    print("Friendships" + "\n" + "______________")

    with open(fileName, 'r', encoding='utf-8') as infile:
        infile = infile.read().split('\n')

        for line in infile:
            words = line.split(" ")
            for word in words:
                if word[0].isupper():
                    if word1 == "":
                        word1 = word
                    else:
                        word2 = word

            names = word1 + " - " + word2
            print(names)
            word1 = ""
            word2 = ""


printFromList('sentences')


# lag også denne med en regex som kan finne ord med store bokstaver
def printAlternative():
    # prøv å legge inn med re.findall(pattern, i), hvor i er hvert ord i en setning som tas inn i en løkke. print(
    # values and format)
    print("hei")
