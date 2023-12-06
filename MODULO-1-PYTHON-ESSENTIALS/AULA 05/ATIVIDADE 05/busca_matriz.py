from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        
        colAtual = len(matrix[0]) -1
        linAtual = 0
        while linAtual < len(matrix) and (colAtual >= 0):
            numeroAtual = matrix[linAtual][colAtual]
            if numeroAtual == target:
                return True
            if numeroAtual > target:
                colAtual -= 1
            else:
                linAtual += 1
        return False
matriz = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matriz1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
           [10,13,14,17,24],[18,21,23,26,30]]
print(len(matriz))
print(searchMatrix(matriz1, 29))