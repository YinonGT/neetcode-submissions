class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)== 0:
            return 0
        last = nums[0]
        count = 1
        nums = sorted(nums)
        biggest = 1
        print(nums)
        for i in range(0,len(nums)):
            if last + 1 == nums[i]:
                count += 1
            elif last == nums[i]:
                pass
            else:
                count = 1
            biggest = max(biggest,count)
            last = nums[i]

        return biggest 