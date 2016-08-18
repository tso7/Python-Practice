tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            colWidths[i] = max(colWidths[i], len(tableData[i][j]))
    maxLength = max(colWidths)
    # Display the table
    for j in range(len(tableData[i])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(maxLength), end = '')
        print ('\n')

printTable()
