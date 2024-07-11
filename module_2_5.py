def get_matrix(n: int, m: int, value: int):
    matrix = []
    if n > 0 and m > 0 and value > 0:
        for i in range(n):
            matrix.append([])
        for i in matrix:
            for j in range(m):
                i.append(value)
        return matrix
    else:
        return []


result01 = get_matrix(2, 5, 10)
result02 = get_matrix(2, 2, 0)
result03 = get_matrix(2, 0, 2)
result04 = get_matrix(0, 2, 2)
print(result01)
print(result02)
print(result03)
print(result04)
