def printTable(table):
    colWidths = []    
    for i in range(0, len(table)):
        colWidth = 0
        for j in range(0, len(table[i])):
            if len(table[i][j]) > colWidth:
                colWidth = len(table[i][j])
        colWidths.append(colWidth)
    # print(colWidths)
    maxWidth = max(colWidths)
    for i in range(0, len(table[i])):
        for j in range(0, len(table)):
            print(table[j][i].rjust(maxWidth), end=' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)