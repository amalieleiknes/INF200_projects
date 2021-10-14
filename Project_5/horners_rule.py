import Project_4.convert_list as one
import Project_4.convert_list_2 as two

polynom_values_dict = {"Polynomial": [], "x": [], "Expected": [4, 5, 6, 4.750, 1027], "Computed": []}


def polynom_calc(a, x):  # where a is a list of different values for a
    # and the place in the list is the a_value

    mattestykker = []
    listLength = len(a)
    sum = 0

    # format and add the polynoms to the first list in dictionary
    for i in range(listLength - 1, -1, -1):  # motsatt for-løkke fordi den med høyest x-verdi er først
        a_value = a[i]  # a-verdien
        if a_value > 0 and i != listLength - 1:
            mattestykker.append("+")
        if a_value != 0:
            if i == 0:
                mattestykker.append(str(a_value))
                sum += a_value
            else:
                if a_value == 1:
                    mattestykker.append("x^")
                    mattestykker.append(str(i))
                    sum += (x ** i)
                else:
                    if i == 1:
                        mattestykker.append(str(a_value))
                        mattestykker.append("x")
                        sum += (a_value * x)
                    else:
                        mattestykker.append(str(a_value))
                        mattestykker.append("x^")
                        mattestykker.append(str(i))
                        sum += a_value*(x ** i)

    # adding the values to the dictionary
    polynom_values_dict["Polynomial"].append(''.join(mattestykker))
    polynom_values_dict["x"].append(x)
    polynom_values_dict["Computed"].append(sum)

    # TODO gjør om til DF
    # table = pd.DataFrame(data=polynom_values_dict)
    return polynom_values_dict


if __name__ == "__main__":
    for polynom in ([[4], 0],
                    ([[5, -2, 3], 0]),
                    ([[5, -2, 3], 1]),
                    ([[5, -2, 3], 0.5]),
                    ([[3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 2])):
        polynom_calc(polynom[0], polynom[1])
    print(polynom_values_dict)

    # records = (one.to_records(polynom_values_dict))

    # print(two.to_dataframe(records))
