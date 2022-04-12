# sorting both string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        
        if s == t:
            return True
        else:
            return False
            
  Time Complexity: O(nlogn)
  Space Complexity: O(1)
    
#In-Short    
def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)
    
#using Hashmap 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        counter = {}
            
        if len(s) != len(t):
            return False
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
        
        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False
            
        for val in counter.values():
            if val != 0:
                return False
        
        return True
      
      TC = O(n)
      SC = o(1)
