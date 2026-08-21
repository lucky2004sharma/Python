def matrix_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
 
 
def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError("Incompatible matrix dimensions for multiplication")
 
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(cols_a))
    return result
 
 
def matrix_transpose(m):
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
 
 
def print_matrix(m, label=""):
    if label:
        print(label)
    for row in m:
        print(row)
    print()
 
 
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
 
    print_matrix(matrix_add(A, B), "A + B:")
    print_matrix(matrix_multiply(A, B), "A x B:")
    print_matrix(matrix_transpose(A), "Transpose of A:")