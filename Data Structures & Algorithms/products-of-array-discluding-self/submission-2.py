class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        nzero = 0
        narr = []
        zindex = 0
        
        for index,val in enumerate(nums):
            if not val == 0 :
                total = total*val
            else:
                nzero = nzero +1 
                zindex = index
        if nzero >=2:
            return [0 for i in range(len(nums))]
        for index,val in enumerate(nums):
            if nzero == 0 :
                narr.append(total//val)
            else:
                if index == zindex:
                    narr.append(total)
                else:
                    narr.append(0)
            

        return narr

        