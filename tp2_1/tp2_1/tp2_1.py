def main(n_edificios: int, k_visibles: int) -> int:
    opt = [[0] * (k_visibles + 2) for _ in range(n_edificios + 2)]
    opt[1][1] = 1
    for i in range(2, n_edificios + 1):
        for j in range(1, k_visibles + 1):
            if j > i:
                break
            opt[i][j] = opt[i - 1][j - 1] + (i - 1) * opt[i - 1][j]

    return opt[n_edificios][k_visibles]
