class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Hmap = {}
        
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in Hmap:
                return [Hmap[diff],idx]
            Hmap[val] = idx
        return