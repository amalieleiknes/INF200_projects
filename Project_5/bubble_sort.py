
def bubble_sort(in_data):
    sortedList = list(in_data)
    length_list = len(sortedList)
    print("Data: ", in_data)
    print("Copied List: ", sortedList)
    print("Length on sortedList: ", len(sortedList))

    if len(sortedList) == 0:
        return sortedList
    else:

        # for-løkke som går nedover fra listelengde-1 (fordi index=0) til 0, slik at
        # neste løkke kan bruke den som utgangspunkt for hvor langt i løkka den skal fortsette å boblesortere
        for n in range(length_list-1, 0, -1):

            for i in range(n):

                this_number = sortedList[i]
                next_number = sortedList[i + 1]
                if this_number > next_number:
                    sortedList[i] = next_number
                    sortedList[i+1] = this_number

        return sortedList


if __name__ == "__main__":
    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
        print("")
