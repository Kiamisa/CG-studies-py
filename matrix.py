import numpy as np

class Matrix:
    def __init__(self):
        pass
    
    def matrix_d1(self):
        output = np.random.rand(3)
        return output
    
    def matrix_d3(self):
        output = np.random.rand(3,3)
        return output
    
    def identity(self, size=3):
        output = np.eye(size)
        return output
    
    def zeros(self, rows=3, col=3):
        output = np.zeros((rows, col))
        return output
    
    def opposite_matrix(self, matrix):
        output = -matrix
        return output


def main():
    saida = Matrix()
    result = saida.matrix_d1()
    print(f"A saída de uma matriz unidimensional é \n{result}")

    original_matrix = saida.matrix_d3()
    print(f"A saída de uma matriz tridimensional é \n{original_matrix}")

    result = saida.identity()
    print(f"A saída de uma matriz identidade 3x3 é \n{result}")

    result = saida.zeros()
    print(f"A saída de uma matriz nula 3x3 é \n{result}")

    result = saida.opposite_matrix(original_matrix)
    print(f"A saída de uma matriz oposta 3x3 é \n{result}")


if __name__ == "__main__":
    main()