# se dokumentasjon på pandas og matplotlyb
import time


# printing out the head of the input file
def head(fileName, numberOfLines=5):
    print("Head: " + str(numberOfLines))
    with open(fileName, 'r', encoding='utf-8') as infile:
        infile = infile.read().strip().split('\n')
        count = 1
        for line in infile:
            if count <= numberOfLines:
                print(line)
                count += 1
            else:
                break


"""     One could also use range, but would need some further adjustments
        for line in range(numberOfLines):
            print(infile[line])
"""

head('norway_municipalities_2017.csv', 1)
head('sample', 4)
print("\n")

# printing out the tail of the input file
def tail(fileName, numberOfLines=5):
    print("Tail: " + str(numberOfLines))
    with open(fileName, 'r', encoding='utf-8') as infile:
        infile = infile.read().strip().split('\n')
    count = 0
    for line in reversed(infile):
        if count < numberOfLines:
            print(line)
            count += 1
        else:
            break


startTail = time.time()
tail('norway_municipalities_2017.csv', 1)
tail('sample', 4)
endTail = time.time()
print("Tail, time: ", endTail - startTail, "\n")


# printing out the tail without reading the whole file first
def fasterTail(fileName, numberOfLines=5):
    print("Faster tail: " + str(numberOfLines))

    with open(fileName, 'r', encoding='utf-8') as infile:
        for line in (infile.readlines()[-numberOfLines:]):
            print(line, end="")


start = time.time()
fasterTail('norway_municipalities_2017.csv', 1)
fasterTail('sample', 4)
end = time.time()
print("\nFasterTail, time: ", end - start)
