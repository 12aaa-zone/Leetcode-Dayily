from typing import List


class Solution:
    """
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            print(f" {dp[i]} ")
        return max(dp)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        pre = 0
        res = nums[0]

        for i in range(size):
            pre = max(nums[i], pre + nums[i])
            res = max(res, pre)
        return res


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution = Solution()

print(f" res is {solution.maxSubArray(nums)} ")
