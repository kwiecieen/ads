from kol3testy import runtests


def orchard(T, m):
    n = len(T)
    total_sum = sum(T)
    target_remainder = total_sum % m

    # Jeśli suma już jest podzielna przez m, nie trzeba nic ciąć
    if target_remainder == 0:
        return 0

    # dp[i][r] = minimalna liczba elementów z pierwszych i elementów
    # które dają resztę r przy dzieleniu przez m
    INF = float('inf')
    dp = [[INF] * m for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        for r in range(m):
            if dp[i][r] == INF:
                continue

            # Nie bierzemy elementu T[i]
            dp[i + 1][r] = min(dp[i + 1][r], dp[i][r])

            # Bierzemy element T[i]
            new_remainder = (r + T[i]) % m
            dp[i + 1][new_remainder] = min(dp[i + 1][new_remainder], dp[i][r] + 1)

    return dp[n][target_remainder] if dp[n][target_remainder] != INF else n


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
