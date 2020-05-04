class Solution:
    def findComplement(self, num: int) -> int:
        i=0
        while(pow(2,i)<=num):
            i+=1
        return pow(2,i)-num-1
    
        