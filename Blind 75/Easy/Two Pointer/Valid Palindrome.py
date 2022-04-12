#Two Pointer
#Alphanumeric is a description of data that is both letters and numbers. 
'''
For example, "1a2b3c" is a short string of alphanumeric characters. 
Alphanumeric is commonly used to help explain the availability of text that 
can be entered or used in a field, such as an alphanumeric password field.
'''

def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1
        r -= 1
    return True
  
  
  #Different approach
  
  def isPalindrome(self, s: str) -> bool:
        s= ''.join(char for char in s if char.isalnum()) 
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
        
  
