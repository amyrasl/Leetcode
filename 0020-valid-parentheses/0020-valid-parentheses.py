class Solution:
    def isValid(self, s: str) -> bool:
        the_dict = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        
        stack = []
        
        for ptr in s:
          if ptr in the_dict.values():
            stack.append(ptr)
          elif stack and the_dict[ptr] == stack[-1]:
            stack.pop()
          else:
            return False
        
        return stack == []