def rotate(key):
    new_key = [[0] * len(key) for _ in range(len(key))]

    for i in range(len(key)):
        for j in range(len(key)):
            new_key[j][len(key)-1-i] = key[i][j]
    return new_key