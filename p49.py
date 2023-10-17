import collections
from typing import List


class Solution:
    """
    #哈希序列,每一层储存同类型字符串,每个字符串按照count对字母的按位统计做索引归并
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                # ord函数,获取字符的unicode值,兼容ascii
                counts[ord(ch) - ord("a")] += 1

                # tuple将字符转化为元组,非元组可供列表使用,字典仅能使用元组
            # print(f"{counts}+  高洪波  +{st}")
            mp[tuple(counts)].append(st)

        return list(mp.values())
    """

    def groupAnagrams(self, strs: List[str]) -> list[list[str]]:

        # 创建空字典
        table = {}
        for s in strs:

            # 排序,生成基准序列
            _s = "".join(sorted(s))

            # 基准序列暂时不存在与字典,则新建索引,初始化值的列表,并给值列表第一位赋值s
            if _s not in table:
                table[_s] = [s]
            else:
                table[_s].append(s)

        # 返回字典中所有值
        return list(table.values())


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution.groupAnagrams(strs)

