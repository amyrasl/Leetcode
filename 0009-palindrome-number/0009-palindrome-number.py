class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 and x % 10 == 0):
            return False
        return x == self.reverseNumber(x)
    
    def reverseNumber(self, x):
        flag = 0
        
        while x != 0:
            calc = x % 10
            flag = flag*10 + calc
            x = int(x/10)
            
        return flag