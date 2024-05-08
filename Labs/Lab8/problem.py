def coinChange(self, coins: List[int], amount: int) -> int:
    max_amount = amount + 1
    dp = [max_amount] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != max_amount else -1
