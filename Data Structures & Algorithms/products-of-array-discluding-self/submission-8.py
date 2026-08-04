class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newarr = [1]*len(nums)
        total = 1
        for i in range(len(nums)):
            newarr[i] = newarr[i]*total
            total  = total * nums[i]
            
        total = 1
        for i in range(len(nums)-1,-1,-1):
            newarr[i] = newarr[i]*total
            total  = total * nums[i]
        return newarr
            