class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left = [None] * len(nums)
        from_left[0] = nums[0]
        from_right = [None] * len(nums)
        from_right[-1] = nums[-1]
        for i in range(1, len(nums)):
            from_left[i] = nums[i] * from_left[i-1]
        for i in range(len(nums)-2, -1, -1):
            from_right[i] = nums[i] * from_right[i+1]

        result = [None] * len(nums)
        result[0] = from_right[1]
        result[-1] = from_left[-2]
        for i in range(1, len(nums)-1):
            result[i] = from_left[i-1] * from_right[i+1]

        return result
        