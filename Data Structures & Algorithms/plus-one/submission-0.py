class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0 :
            return 1
        num = 0 
        for i in digits : 
            num=num*10+i
        print(num)
        num+=1
        digits = []
        while num>0:
            digits.append(num%10)
            num = num//10
        return digits[::-1]