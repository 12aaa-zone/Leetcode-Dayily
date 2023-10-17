from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        none_zero_index = 0

        for current in range(len(nums)):
            if nums[current] != 0:
                nums[current], nums[none_zero_index] = nums[none_zero_index], nums[current]
                none_zero_index += 1
            print(current, " and ", none_zero_index," is ", nums)

        nums[none_zero_index:] = [0] * (len(nums) - none_zero_index)


num = [0, 1, 0, 3, 12]

solution = Solution()
solution.moveZeroes(nums=num)
