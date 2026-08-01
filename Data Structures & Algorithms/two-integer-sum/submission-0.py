class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index,val in enumerate(nums):
            if target-val in dic: 
                return [dic[target-val],index]
            dic[val] = index
        return -1
        