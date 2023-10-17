from typing import List

"""
给定一个 m x n 的矩阵，如果一个元素为 0 
则将其所在行和列的所有元素都设为 0 。
*请使用 原地算法 尽可能降低空间复杂。
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False

        # 逐行遍历, 若有某行首列出现0,则标记
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col0 = True
            # 逐字遍历, 若出现零, 则标记行列头
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    print("\n%")
                    print_matrix(matrix)

        # 倒序逐行遍历
        for i in range(m - 1, -1, -1):
            # 逐字遍历,若行列头有标记,则判零
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    print(f"\n& {matrix[i][j]}")
                    print_matrix(matrix)
                    matrix[i][j] = 0

            # 若头列有标记,说明头列全零
            if flag_col0:
                matrix[i][0] = 0

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")  # 输出元素并用空格分隔
        print()  # 换行


# 示例用法
matrix = [[1,2,3,4],
          [5,0,7,8],
          [0,10,11,12],
          [13,14,15,0]]

solution = Solution()
solution.setZeroes(matrix)

# 遍历矩阵并输出每一行的元素
for row in matrix:
    for element in row:
        print(element, end=" ")  # 输出元素并用空格分隔
    print()  # 换行
