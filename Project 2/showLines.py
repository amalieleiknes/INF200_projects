# printing out the head of the file
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


head('norway_municipalities_2017.csv', 1)


# printing out the tail
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


tail('norway_municipalities_2017.csv', 1)


def fasterTail(fileName, numberOfLines=5):
    print("Faster tail: " + str(numberOfLines))

    with open(fileName, 'r', encoding='utf-8') as infile:
        for line in (infile.readlines()[-numberOfLines:]):
            print(line, end="")


fasterTail('norway_municipalities_2017.csv', 2)
