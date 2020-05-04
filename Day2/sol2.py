class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic={}
        for i in S:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        count=0
        for i in J:
            if i in dic:
                count+=dic[i]
        return count