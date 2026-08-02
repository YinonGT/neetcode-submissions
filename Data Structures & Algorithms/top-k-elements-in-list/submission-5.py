class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        arr = [[] for i in range(len(nums))]

        dic = {}

        for val in nums:
            dic[val] = 1+dic.get(val,0)

        for key,val in dic.items():
            arr[val-1].append(key)

        ans = []

        for i in range(len(arr)-1,-1,-1):
            for j in arr[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        return []

        