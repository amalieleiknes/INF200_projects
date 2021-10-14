import pandas as pd


list1 = [{'name': 'Joe', 'age': 22, 'phone': '12345678'},
         {'name': 'Pia', 'age': 24, 'phone': '23456789'},
         {'name': 'Even', 'age': 21, 'phone': '34567890'},
         {'name': 'Abdul', 'age': 23, 'phone': '45678901'}]

list2 = []

list3 = [{'name': 'Joe', 'phone': '12345678'},
         {'name': 'Pia', 'phone': '23456789'},
         {'name': 'Even', 'phone': '34567890'},
         {'name': 'Abdul', 'phone': '45678901'}]

list4 = [{'name': 'Joe', 'age': 22, 'phone': '12345678'},
         {'name': 'Pia', 'age': '', 'phone': '23456789'},
         {'name': 'Even', 'age': 21, 'phone': '34567890'},
         {'name': 'Abdul', 'phone': '45678901'}]


def to_dataframe(data):
    if len(data) == 0:
        return "No data available"
    # should also check if column is missing from DF
    # should also output what rows are missing what values in the different columns and if format on cellvalue is OK
    else:
        df = pd.DataFrame(data=data)
        average_age = df['age'].mean()
        return average_age


# print(to_dataframe(list1))
# print(to_dataframe(list2))
# print(to_dataframe(list3))

