class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newarr = [1]*len(nums)
        total = 1
        for i in range(len(nums)):
            total  = total * nums[i]
            if not i == len(nums)-1:
                newarr[i+1] = newarr[i+1]*total
        total = 1
        for i in range(len(nums)-1,-1,-1):
            total  = total * nums[i]
            if not i == 0:
                newarr[i-1] = newarr[i-1]*total
        return newarr
            