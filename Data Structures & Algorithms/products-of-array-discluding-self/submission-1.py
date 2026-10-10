class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]
        prod = 1
        for i in range(1,len(nums)):
            prod *= nums[i - 1]
            left_prod.append(prod)
        right_prod = [1]
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            right_prod.append(prod)

        
        return [ x * y for x, y in zip(left_prod, right_prod[::-1])]