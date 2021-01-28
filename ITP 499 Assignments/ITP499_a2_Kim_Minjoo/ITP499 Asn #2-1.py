def filter_list(stringList, string):
    # stringList = list of all the strings
    # string = a string to match

    outputList = []
    charList = []       # Made a charList to put each letter of the matching string ex) "o", "u", "r"
    count = 0           # This count variable is used to keep track of count of each letter in the string

    # checking if the stringList input is a list and string is str
    if isinstance(stringList, list) and isinstance(string, str):

        for i in range(len(string)):            # put each character in the string into charList
            charList.append(string[i])          # this will be used compare each character in the string with the
                                                    # the strings in the list
        # Loop through the entire stringList
        for a in range(len(stringList)):
            # For each item in the stringList, loop through each character in the string
            for i in range(len(string)):
                # For each character in the string in the list,
                for j in range(len(stringList[a])):
                    # check if character from the string matches with each character of a string within the stringList
                    if string[i] == (stringList[a][j]):
                        # if the character from the string (our) and from the word within stringList
                        # are the same, count +=1
                        count += 1

            if count == len(charList):
                outputList.append((stringList[a]))

            # reset the count variable if this is all over
            count = 0

        return outputList

    else:
        print("Invalid input. Please try again.")
