class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count =0
        max_c =0 
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
            elif nums[i] ==0:
                count =0
            if count > max_c:
                max_c = count

        
        return max_c
