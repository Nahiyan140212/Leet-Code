#Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]
  TC: O(n*n)
  SC: O(1)
    
    
#Using Hashmap:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap =  {}
        
        for i in range(len(nums)):
            k = target - nums[i]
            if k in hashmap:
                return [i, hashmap[k]]
            else:
                hashmap[nums[i]] = i
                
                
  TC: O(n)
  SC: O(n)
