class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = []

        # prefx fill
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]

        # suffix fill
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        
        # combine prefix and suffix
        for i in range(len(prefix)):
            output.append(prefix[i] * suffix[i])

        return output