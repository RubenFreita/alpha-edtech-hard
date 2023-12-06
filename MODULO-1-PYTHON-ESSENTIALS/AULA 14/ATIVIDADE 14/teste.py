def min_positions_for_stables(n, m, positions):
    positions.sort()  # Ordena as posições das vacas para facilitar o processamento
    k = len(positions)
    dp = [[float('inf')] * (m + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for i in range(1, k + 1):
        for j in range(1, m + 1):
            for l in range(i):
                cost = positions[i - 1] - positions[l] + 1
                dp[i][j] = min(dp[i][j], dp[l][j - 1] + cost)
                
    print(dp)
    return dp[k][m]

# Exemplo de uso
n = 20
m = 2
vacas = [3, 12, 13, 15]
resultado = min_positions_for_stables(n, m, vacas)
print(resultado)