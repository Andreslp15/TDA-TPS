def main(n_edificios: int, k_visibles: int) -> int:
    opt = [[0] * (k_visibles + 1) for _ in range(n_edificios + 1)]
    opt[0][0] = 1
    for i in range(1, n_edificios + 1):
        for j in range(1, k_visibles + 1):
            if j > i:
                break
            opt[i][j] = opt[i - 1][j - 1] + (i - 1) * opt[i - 1][j]
    return opt[n_edificios][k_visibles]
