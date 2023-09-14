#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for i in range(len(matrix)):
        new_list.append(list(map(lambda x: x ** 2, matrix[i])))

    return new_list
