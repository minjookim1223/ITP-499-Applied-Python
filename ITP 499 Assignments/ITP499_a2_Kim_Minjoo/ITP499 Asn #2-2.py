# x will be the number of rows and y will be the number of columns
# in other words, make x number of lists that are y long


def generate_matrix(x, y):
    # matrix will be a list of lists
    matrix = []

    # accounting for special cases
    # if x is the same as y (in other words, n x n matrix)
    if x == y:
        for i in range(x):
            row = []                    # initialize a row to append to the matrix
            for j in range(y):          # loop through length of y,
                if i == j:              # when i == j, the value has to be 10
                    row.append(10)
                else:                   # otherwise, same as instructed (value = i*j)
                    row.append(i * j)
            matrix.append(row)          # append the row to the matrix (the list of lists)

    else:                               # basically repeat the process above except for the special case
        for i in range(x):
            row = []
            for j in range(y):
                row.append(i*j)
            matrix.append(row)

    return matrix
