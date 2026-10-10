class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums) - 1
        lo = 0
        mid = (hi) // 2

        while lo <= hi:
            k = nums[mid]
            if k == target:
                return mid
            if k > target:
                hi = mid - 1
                mid = (hi + lo) // 2
            if k < target:
                lo = mid + 1
                mid = (hi + lo) // 2    

        return -1    