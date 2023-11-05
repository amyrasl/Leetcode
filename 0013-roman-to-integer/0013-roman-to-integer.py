class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        sum = 0
        for ptr in range(len(s)):
          if ptr+1 < len(s) and roman_dict[s[ptr]] < roman_dict[s[ptr + 1]]:
            sum = sum - roman_dict[s[ptr]]
          else:
            sum = sum + roman_dict[s[ptr]]
        
        return sum