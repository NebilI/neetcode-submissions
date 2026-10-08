class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        min_cost_dict = {i: float('inf') for i in range(len(cost))}

        for i in range(0, len(cost)):
            if i < 2:
                min_cost_dict[i] = cost[i]
            else:
                min_cost_dict[i] = min(min_cost_dict[i-1],min_cost_dict[i-2]) + cost[i]
        print(min_cost_dict)
        return min(min_cost_dict[len(cost)-1],min_cost_dict[len(cost)-2])