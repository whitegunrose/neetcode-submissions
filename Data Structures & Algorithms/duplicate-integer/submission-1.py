class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # keep track of values we have seen
        # Compare them to values we will look at later
        seen = set()

        # loop through given array
        for num in nums:
            if num in seen:
                # we have a duplicate
                return True
            # else
            # add to seen to keep track
            seen.add(num)
        return False
            
        