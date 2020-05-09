class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=0
        while(i*i<=num):
            if(i*i==num):
                return 1
            i+=1
        return 0