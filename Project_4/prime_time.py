import numpy as np


def find_primes(n, s=1):
    numberList = list(range(s, n + 1))

    for i in numberList:
        if i % 2 == 0 and i != 2:
            numberList.remove(i)

    for i in numberList:
        if i % 3 == 0 and i != 3:
            numberList.remove(i)

    for i in numberList:
        if i % 5 == 0 and i != 5:
            numberList.remove(i)

    for i in numberList:
        if i % 7 == 0 and i != 7:
            numberList.remove(i)

    return numberList


def find_primes_numpy(n, s=1):
    numpyArray = np.array(range(s, n + 1))

    numpyArray = np.delete(numpyArray, np.where((numpyArray % 2 == 0) & (numpyArray > 2)))
    numpyArray = np.delete(numpyArray, np.where((numpyArray % 3 == 0) & (numpyArray > 3)))
    numpyArray = np.delete(numpyArray, np.where((numpyArray % 5 == 0) & (numpyArray > 5)))
    numpyArray = np.delete(numpyArray, np.where((numpyArray % 7 == 0) & (numpyArray > 7)))

    return numpyArray


def find_primes_pythonSet(n, s=1):
    numberSet = set(list(range(s, n + 1)))

    copiedSet = numberSet.copy()
    for i in numberSet:
        if i % 2 == 0 and i != 2 or i % 3 == 0 and i != 3 or i % 5 == 0 and i != 5 or i % 7 == 0 and i != 7:
            copiedSet.remove(i)

    return copiedSet


print("Python list: ", find_primes(10**4))
print("Numpy array: ", find_primes_numpy(10**4))
print("Python set: ", find_primes_pythonSet(10**4))
