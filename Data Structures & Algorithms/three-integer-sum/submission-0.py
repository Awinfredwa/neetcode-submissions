class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1, n-1):
                target =  - (nums[i] + nums[j])
                #binary search from j+1 to end
                l = j+1
                r = n-1
                while(l<=r):
                    m = int((l+r)/2)
                    # if nums[l] == target:
                    #     res.add((nums[i], nums[j], nums[l]))
                    #     break
                    # if nums[r] == target:
                    #     res.add((nums[i], nums[j], nums[r]))
                    #     break
                    if nums[m] == target: 
                        res.add((nums[i], nums[j], nums[m]))
                        break
                    elif nums[m] > target:
                        r = m-1
                    else:
                        l = m+1
        return list(res)
# -4, -1, -1, 0, 1, 2 

        