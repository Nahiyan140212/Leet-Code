##Using hashSet
class Solution:
    def containsDuplicate(self, nums):
		#creating a set where only the unique value will be stored. If there is no repeated value then the length of seen and length will be the same.
		
	seen = set(nums)
	if len(seen) == len(nums):
		return False
	else:
		return True
  
  
  
  ##Brute Force
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
  
  
  
  ##Using Hashmap
  
  class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = i
        return False
        
  
