class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicw = defaultdict(list)
        for index,val in enumerate(strs):
            arr = [0]*26
            for i in val:
                arr[ord(i)-ord('a')] +=1
            dicw[tuple(arr)].append(val)
        return list(dicw.values())