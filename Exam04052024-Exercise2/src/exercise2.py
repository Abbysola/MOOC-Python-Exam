# Write your solution to exercise 2 here
def copy(matrix: list):
    copy_of_original = []
    for row in matrix:
        copy_row = row[:]
        copy_of_original.append(copy_row)
    return copy_of_original 

def flip(matrix:list):
    for row in matrix:
        row.reverse()       
                       
def flip_and_copy(matrix:list): 
    copied_matrix = copy(matrix) 
    matrix = copied_matrix
    flipped_copy = flip(copied_matrix)   
    return flipped_copy

