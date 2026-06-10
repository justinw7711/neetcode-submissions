class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for i in range(len(nums)):
            duplicate.add(nums[i])
        if len(duplicate) ==  len(nums):
            return False
        else:
            return True
        
            
                
            
            