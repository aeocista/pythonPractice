#! python 3

tableData = [['apples', 'oranges', 'cherries', 'bananas',
              'Alice', 'Bob', 'Cynthia', 'Dorene',
              'dogs', 'eels', 'ferrets', 'giraffes']]


def printTable(tableData, colWidths):
    print('THINGS AND PEOPLE I LIKE')
    for k, v in tableData.items():
        colWidths = [0] * len(tableData)
        print(k.rjust(colWidths, '.') + str(v).rjust(colWdiths))

        
printTable(tableData, 20)
              
