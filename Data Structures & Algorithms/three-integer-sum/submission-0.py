class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # output array
        out = []

        # start by sorting array
        nums.sort()

        # iterate through sorted array, and this becomes Two Sum II
        for i, num in enumerate(nums):

            # skip dulpicates
            # idx > 0 means we're looking at nums[1:]
            if i > 0 and num == nums[i - 1]:
                continue

            # indicies of pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:

                # compute threesum
                threeSum = num + nums[left] + nums[right]

                # two sum is too big
                # move right pointer to left
                if threeSum > 0:
                    right -= 1

                # two sum is too small
                # move left pointer to right
                elif threeSum < 0:
                    left += 1

                # found a pair
                else:
                    out.append([num, nums[left], nums[right]])

                    # move left pointer to look for other two sums
                    # skip over duplicates
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1


        return out