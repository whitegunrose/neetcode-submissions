class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Hash Map
        # Python dictionaries
        # {key : value, 
        # ...
        # }

        # Key: value
        # Value: index
        prevMap = {}

        # for (int i = 0; i < ..; i++)
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], idx]
            prevMap[num] = idx