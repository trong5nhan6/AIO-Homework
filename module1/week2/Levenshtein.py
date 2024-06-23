def levenshtein_distance(token1, token2):
    s1 = len(token1)
    s2 = len(token2)

    matrix = [[0 for _ in range(s2+1)] for _ in range(s1+1)]\

    for i in range(s1 + 1):
        matrix[i][0] = i
    for j in range(s2 + 1):
        matrix[0][j] = j

    for i in range(1, s1 + 1):
        for j in range(1, s2 + 1):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(matrix[i-1][j] + 1,       # Xóa (deletion)
                               matrix[i][j-1] + 1,      # Thêm (insertion)
                               matrix[i-1][j-1] + cost)  # Thay thế (substitution))

    return matrix[s1][s2]


token1 = 'hola'
token2 = 'hello'
print(levenshtein_distance(token1, token2))
