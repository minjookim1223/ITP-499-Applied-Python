# Minjoo Kim
# ITP 499
# Assignment #5
# 3/1/2020

import numpy as np


def numpy_divide_or_multiply(a, b, operation="no input"):
    if operation == "multiply":
        return np.multiply(a, b)

    elif operation == "divide":
        return np.divide(a, b)

    else:
        print("Error")
        return "Error"


def numpy_reverse_array(arr):
    return np.flip(arr)


def numpy_random_computations(x, op="None"):
    arr = np.array([np.random.rand() for i in range(x)])

    if op == "AVG":
        return np.mean(arr)
    elif op == "VAR":
        return np.var(arr)
    elif op == "SD":
        return np.std(arr)
    else:
        print("Error in optional input.")
        compTuple = (np.mean(arr), np.var(arr), np.std(arr))
        return compTuple


def numpy_occurrences(numArray):
    if type(numArray) is np.ndarray:
        uniqueDict = {}
        uniqueArray, countArray = np.unique(numArray, return_counts=True)

        for i in range(uniqueArray.size):
            uniqueDict[str(uniqueArray[i])] = countArray[i]
            print(i)

        return uniqueDict

    else:
        print("Error")
        return "Error"