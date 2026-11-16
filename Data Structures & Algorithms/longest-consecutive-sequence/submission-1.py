class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet: set = set(nums)
        longest: int = 0

        for i in nums:

            # check if i is start of sequence
            # if i - 1 is in set, it is not a start of sequence
            # if i - 1 is NOT in set, it IS start of sequence
            if (i - 1) not in numSet:
                length: int = 0
                while (i + length) in numSet:
                    length += 1
                longest: int = max(length, longest)
        return longest