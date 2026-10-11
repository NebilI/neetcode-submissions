class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        num_check = 2 ** len(nums) - 1

        subsets = set()

        for i in range(0, num_check+1):
            subset = []
            for j in range(0, len(nums)):
                to_insert = (i >> j) & 1
                if to_insert == 1:
                    subset.append(nums[j])
            subset.sort()
            x = tuple(subset)
            if x not in subsets:
                subsets.add(x)
        
        return [list(x) for x in subsets]
                    
        
        