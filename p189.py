from typing import List

"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置
其中 k 是非负数。
"""


def reverse(nums: List[int], left, right) -> None:
    i, j = left, right
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        #一,原版语法解决
        n = len(nums)
        k %= len(nums)
        nums = nums[-k:] + nums[:- k]
        """

        # 二,双指针翻转法解决
        n = len(nums)
        k %= n
        # 全逆
        reverse(nums, 0, n - 1)

        # 前逆
        reverse(nums, 0, k - 1)

        # 后逆
        reverse(nums, k, n - 1)


arr = [1, 2, 3, 4, 5, 6, 7]
solution = Solution()
solution.rotate(arr, 3)
print(arr)
