class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s  = set(nums)
        count = 0
        biggest = 0 
        num = 0
        for val in nums:
            if  val-1 not in s:
                num = val 
                count = 0
                while num+count in s:
                    count +=1
                biggest = max(count,biggest)
        return biggest
                