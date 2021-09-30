import re


def markingErrors(inputSentence):
    print(inputSentence)
    count = 0
    for match in re.finditer(r"\b(\w+)\s+\1\b", inputSentence):
        startNext = match.start()
        if count == 0:
            print(' ' * match.start() + '*' * (match.end() - match.start()), end='')
            count += 1
        else:
            print((startNext-endPrev)*" ", end='')
            print('' * match.start() + '*' * (match.end() - match.start()), end='')
        endPrev = match.end()


markingErrors("I can see the the red rose rose and the purple lilac.")

print()

markingErrors("I I I I")
