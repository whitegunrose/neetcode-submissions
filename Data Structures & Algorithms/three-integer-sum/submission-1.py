class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # output array
        out: list = []

        # sort the array
        nums.sort()

        # iterate through the sorted array
        for i, num in enumerate(nums):

            # skip duplicates
            if i > 0 and num == nums[i - 1]:
                continue

            # start with smaller twosum
            # keep track of pointers
            front: int = i + 1
            back: int = len(nums) - 1

            # looping thru like twosum
            while front < back:

                # calculate the threeSum
                threeSum: int = num + nums[front] + nums[back]

                # three sum is too big
                # move right pointer to left
                if threeSum > 0:
                    back -= 1

                # three sum is too small
                # move left pointer to right
                elif threeSum < 0:
                    front += 1

                # found a pair
                else:

                    # append to output array
                    out.append([num, nums[front], nums[back]])

                    front += 1
                    while front < back and nums[front] == nums[front - 1]:
                        front += 1

        return out