class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic1 = {}
        for i in range(len(s)):
            dic1[s[i]] = 1+dic1.get(s[i],0)
            dic1[t[i]] = dic1.get(t[i],0)-1
        for key in dic1:
            if dic1[key] != 0 :
                return False
        return True


        