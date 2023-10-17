import heapq
from typing import List


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n=len(nums)

        q=[(-nums[i], i) for i in range(k) ]

        heapq.heapify()

        return res


solution = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
solution.maxSlidingWindow(nums,k)
