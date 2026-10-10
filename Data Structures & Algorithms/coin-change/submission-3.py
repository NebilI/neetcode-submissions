from functools import cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(remaining, i):
            if remaining == 0:
                return 0
            if remaining < 0 or i == len(coins):
                return float('inf')

            take = 1 + dfs(remaining - coins[i], i)
            skip = dfs(remaining, i + 1)

            return min(take, skip)

        result = dfs(amount, 0)
        return result if result != float('inf') else -1