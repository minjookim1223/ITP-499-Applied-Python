from operator import itemgetter, attrgetter


def tupleSeparator(string):
    # Split the string into a list with a delimiter of -
    # Each item in the list will have the name, age, and score all within a single string
    stringList = string.split("-")
    # Initialize a tupleList
    # We will be dividing each string within the list into tuples
    tupleList = []

    # for the length of the stringList
    for i in range(len(stringList)):
        # make a temporary list to split each string within the stringList
        tempList = stringList[i].split(",")
        # make the string into a tuple
        tupleInfo = (tempList[0], tempList[1], tempList[2])
        # attach the tuple made into the list of tuples
        tupleList.append(tupleInfo)

    # when finished return the tupleList, sorted by name, age, then score
    return sorted(tupleList, key=itemgetter(0, 1, 2))
