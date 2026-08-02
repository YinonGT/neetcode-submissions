class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for val in nums:
            dic[val] = 1+dic.get(val,0)
        arr = []
        for i in range(k):
            arr.append(max(dic,key = dic.get))
            dic.pop(max(dic,key = dic.get))
        return arr
        