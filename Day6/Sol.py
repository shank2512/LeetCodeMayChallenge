class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times=len(nums)//2
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
                if dic[i]>times:
                    return i
            else:
                dic[i]=1
                if dic[i]>times:
                    return i
                
        