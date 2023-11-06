class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        firstvar = strs[0]
        lastvar = strs[-1]
        result = ""
        
        for i in range(len(firstvar)):
            if (firstvar[i] != lastvar[i]):
                break
            result += firstvar[i]
        
        return result