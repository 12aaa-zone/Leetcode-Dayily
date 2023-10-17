from typing import List

"""
以数组 intervals 表示若干个区间的集合
其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组
该数组需恰好覆盖输入中的所有区间 。
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        # 储存一个有序的不重复区间
        merged = []

        for interval in intervals:

            # 若结果列表暂时为空，或者最大保留区间的右边界小于新区间左边界
            # 说明不重叠，直接加入
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            # 最大保留区间右边界尝试更新
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
