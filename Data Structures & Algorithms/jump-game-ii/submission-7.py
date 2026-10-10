class Solution:
    def jump(self, nums: List[int]) -> int:

        min_jumps = [0] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            amount_to_jump = nums[i]
            if i + amount_to_jump >= len(nums) - 1:
                min_jumps[i] = 1
            elif amount_to_jump != 0:
                l = list(nums[t] for t in range(i + 1, amount_to_jump + i + 1))
                print(i, nums[i], l)
                min_jumps[i] = 1 + min(min_jumps[t] for t in range(i + 1, amount_to_jump + i + 1))
            else:
                min_jumps[i] = float('inf')
        
        print(min_jumps)
        return min_jumps[0]
            

            