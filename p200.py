from typing import List

"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。
你可以 按任意顺序 返回答案。
示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):  # first代表当前填充位

            if first == n:  # 遍历结束
                res.append(nums[:])  # 则储存结果

            for i in range(first, n):  # 有五种递归分支,每分支填充五层,每层因为i的不同而不同
                nums[first], nums[i] = nums[i], nums[first]  # 交换填充位(first) 和 未被填充位(i >= first), first 递增标志者完成前缀填充
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  # 恢复数组,以供下一次递归使用

        n = len(nums)
        res = []
        backtrack()
        return res


nums = [1, 2, 3, 4]
"""
first = 0                1个转换数组
first = 1  i= 1,2,3,4    1*4个转换数组
first = 2  i= 2,3,4      1*4*3个转换数组
...

1*4*3*2 个全排列数组,保证数量足够,且绝不重复(由交换来达成复用排除),则获得答案
"""

solution = Solution()

print(solution.permute(nums))
