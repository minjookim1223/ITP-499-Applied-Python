class MyNumbers:
    def __init__(self, myList):
        self.myList = myList
        self.myList.reverse()
        self.count = 0

    def __iter__(self):
        self.a = self.myList[self.count]
        return self

    def __next__(self):
        num = self.a
        self.a = self.myList[self.count]
        self.count += 1
        return self.a


def main():
    myList = [10, 11, 12, 13, 14]

    myClass = MyNumbers(myList)
    myIter = iter(myClass)

    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))


main()

