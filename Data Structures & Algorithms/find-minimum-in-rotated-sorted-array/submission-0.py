class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            if r-l==1:
                return min(nums[l],nums[r])
            m = int((l+r)/2)
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                if nums[m]>nums[l]:
                    l = m
                else:
                    r = m
        return -1


        # cases 
        # l <= r: l must be min 
        # l > r: 
            # m > l: min is from m+1 to r
            # m < l: min is from l to m-1 
        