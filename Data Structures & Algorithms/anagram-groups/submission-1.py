class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicw = {}
        for index,val in enumerate(strs):
            arr = [0]*26
            for i in val:
                arr[ord(i)-ord('a')] +=1
            t = tuple(arr)
            if t in dicw:
                dicw[t].append(val)
            else:
                dicw[t] = [val]
        arr = []
        for keys,vals in dicw.items():
            arr.append(vals)
        return arr
            


        
        