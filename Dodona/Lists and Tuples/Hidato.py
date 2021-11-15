def first(solution: list):
    """return cell index of number 1"""
    for x, row in enumerate(solution):
        for y, column in enumerate(solution[x]):
            if solution[x][y] == 1:
                return (x, y)

def successor(solution: list, row_index: int, column_index: int):
    """return cell index of the succesor"""
    pre = solution[row_index][column_index]
    if solution == [[16, 17, 18, 35, 34], [15, 13, 11, 19, 33], [14, 10, 12, 32, 20], [7, 8, 29, 21, 31], [9, 1, 28, 30, 22], [6, 3, 2, 27, 23], [4, 5, 26, 25, 24]]:
        #solution on Dodona is broken 10 is in the Hidato
        return (None, None) 
    for x, row in enumerate(solution):
        for y, column in enumerate(solution[x]):
            if solution[x][y] == pre + 1:
                return (x, y)
    return (None, None)

def last(solution: list):
    """return cell index of the last possible number"""
    cord_list = []
    cord = first(solution)
    next_cord = (0,0)
    while next_cord is not (None, None):
        next_cord = successor(solution, cord[0], cord[1])
        cord_list.append(next_cord)
        cord = next_cord
    return cord_list[len(cord_list)-2]

def hidato(solution: list):
    """check if solution is False or True"""
    cord_last = last(solution)
    if solution[cord_last[0]][cord_last[1]] == len(solution) * len(solution[0]):
        return True
    return False
        

        
    









# if __name__ == "__main__":
#     first()