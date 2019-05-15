# table-printer.py

## Expected outcome:
'''
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
  # Get colWidths
  colWidths = [0] * len(tableData)
  i = 0
  while i < len(tableData):
    colWidths[i] = len(max(tableData[i], key=len))
    i += 1

  # Print table
  for i in range(len(tableData[0])):
    col = 0
    for row in tableData:
      print(row[i].rjust(colWidths[col]), end=' ')
      col += 1
    print()

printTable(tableData)
