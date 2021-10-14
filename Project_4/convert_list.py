# Function takes in a dictionary of lists and should output a list of records. i.e. a list of dictionaries???

list1 = {'name': ['Joe', 'Pia', 'Even', 'Abdul'],
         'age': [22, 24, 21, 23],
         'phone': ['12345678', '23456789', '34567890', '45678901']}


def to_records(data):
    number_of_elements_in_list = len(data[list(data.keys())[0]])

    # checks if data is none or if length of lists in dictionary are empty
    if number_of_elements_in_list == 0:
        return "Input data is empty!"

    # checks if the number of elements in every list is the same
    for key in data.keys():
        if len(data[key]) != number_of_elements_in_list:
            return "Not equal list length in all key sets!"

    listFinal = []

    for n in range(number_of_elements_in_list):
        dataList = {}

        # først går den gjennom nøklene. Altså, den går først gjennom hele nøkkel keyen
        for key in data.keys():
            keyIndex = list(data.keys()).index(key)

            dataList[key] = data[list(data.keys())[keyIndex]][n]
        listFinal.append(dataList)

    return listFinal


# print(to_records(list1))
