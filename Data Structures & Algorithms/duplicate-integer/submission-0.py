class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for index,val in enumerate(nums):
            if val in dic :# dont use dic[val]!= None
                return True
            dic[val] = index
        return False

        