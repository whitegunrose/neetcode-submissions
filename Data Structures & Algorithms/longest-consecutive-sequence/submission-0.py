class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet: set = set(nums)
        longest = 0

        for i in nums:

            # check if i is start of sequence
            # if i - 1 is in set, it is not a start of sequence
            # if i - 1 is NOT in set, it IS start of sequence
            if (i - 1) not in numSet:
                length = 0
                while (i + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest