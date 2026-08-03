class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        biggest = 1 
        count  = 1
        last = nums[0]
        for i in range(len(nums)):
            if last+1 == nums[i]:
                count+=1
            elif last == nums[i]:
                pass
            else:
                count = 1
            last = nums[i]
            biggest = max(biggest,count)
        return biggest 
        
        