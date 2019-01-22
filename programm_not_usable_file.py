def strLIST(q):
    for i in range(len(q)):
        for j in range(len(q[i])):
            if q[i][j] == (-2, 0):
                q[i][j] = 'None'
            else:
                q[i][j] = '(' + str(q[i][j][0]) + ', ' + str(q[i][j][1]) + ')'
    return q

def printLIST(q, name):
    a = []
    for i in range(len(q)):
        a.append('[' + ', '.join(q[i]) + ']')
    a = ',\n'.join(a)
    ans = name + ' = [' + a + ']'
    print(ans)
    return ans

def correct_coords(col, row):
    if row >= 0 and col >= 0 and col < 11 and row < len(field[col]):
        return True
    return False

field =  [[None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None]]

# col , row
one = []
two = []
three = []
four = []
for i in range(len(field)):
    one_ = []
    two_ = []
    three_ = []
    four_ = []
    for j in range(len(field[i])):
        col, row  = i, j
        if col < 5:
            one_.append((col - 1, row))
            four_.append((col - 1, row - 1))
            three_.append((col + 1, row))
            two_.append((col + 1, row + 1))
        elif col == 5:
            one_.append((col - 1, row))
            four_.append((col - 1, row - 1))            
            three_.append((col + 1, row - 1))
            two_.append((col + 1, row))
        else:
            three_.append((col + 1, row - 1))
            two_.append((col + 1, row))
            one_.append((col - 1, row + 1))
            four_.append((col - 1, row))
    one.append(one_)
    two.append(two_)
    three.append(three_)
    four.append(four_)
print(one)
print('')
print(two)
print('')
print(three)
print('')
print(four)
print('')
for i in range(len(field)):
    for j in range(len(field[i])):
        col, row  = i, j
        cell1 = one[col][row]
        cell2 = two[col][row]
        cell3 = three[col][row]
        cell4 = four[col][row]
        if not correct_coords(cell1[0], cell1[1]):
            one[col][row] = (-2,0)
        if not correct_coords(cell2[0], cell2[1]):
            two[col][row] = (-2,0)
        if not correct_coords(cell3[0], cell3[1]):
            three[col][row] = (-2,0)     
        if not correct_coords(cell4[0], cell4[1]):
            four[col][row] = (-2,0)            
printLIST(strLIST(one), 'one')
print('')
printLIST(strLIST(two), 'two')
print('')
printLIST(strLIST(three), 'three')
print('')
printLIST(strLIST(four), 'four')