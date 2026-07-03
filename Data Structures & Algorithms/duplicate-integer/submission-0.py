class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for num in nums:
            if hashmap.get(num) is not None:
                return True # Duplicate Exists
            else:
                hashmap[num] = 1

        return False # Duplicates Do Not Exist
            
        