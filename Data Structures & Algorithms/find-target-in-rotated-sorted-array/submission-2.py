class Solution:
    def bs(self, nums:List[int], target: int, l: int, r: int)->int:
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif target > nums[m]:
                l = m+ 1
            else:
                r = m-1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m 
            if nums[l]<=nums[m]:
                if target>=nums[l] and target <= nums[m]:
                    return self.bs(nums,target,l,m)
                else:
                    l = m+1
            else:
                if target>=nums[m] and target <= nums[r]:
                    return self.bs(nums,target,m,r)
                else:
                    r = m-1
        return -1

        


# target == m: return 
# left side sorted: 
    # target in left: do binary search on left
    # else l = m+1
# right side sorted:
    # target in right: do binary search on right
    # else r = m-1
