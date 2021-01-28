import time
import itertools


def timing(function):
    def innerFunction(*args, **kwargs):
        start = time.time()

        function(*args, **kwargs)

        finish = time.time()
        total = finish - start
        print(function.__name__, "took", finish, "to run")

    return innerFunction


def validation(function):
    def inner(*args, **kwargs):
        classList = []
        for i in args:
            if not isinstance(i, str):
                classList.append(type(i.__name__))
        classList = list(set(classList))
        print("The function expected strings but was inputted, (", str(classList), ")")

    return inner


def fibonacci():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


# izip and chain
def main():
    numList = [34, 36, 38, 40]
    numList2 = [54, 56, 58, 60]
    numCombined = itertools.chain(numList, numList2)
    newNum = list(zip(numList, numList2))
    print(newNum)

    stringList = ["USC", "ITP", "Applied"]
    numList3 = [1, 1, 2020, 2]
    newList = itertools.chain(stringList, numList3)
    newNum = list(zip(stringList, numList3))
    print(newNum)

main()
