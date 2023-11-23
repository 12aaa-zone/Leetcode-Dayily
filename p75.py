from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        if size < 2:
            return

            # 2指针和0指针
        zero_ptr = -1
        two_ptr = size

        # 迭代指针
        i = 0
        while i <= two_ptr - 1:

            # 当前值为0时，更新0指针，将该位置赋值到0指针处，更新迭代器
            if nums[i] == 0:
                zero_ptr += 1
                nums[i], nums[zero_ptr] = nums[zero_ptr], nums[i]
                i += 1

            # 当前值为1时，更新迭代器
            elif nums[i] == 1:
                i += 1

            # 当前值为2时，更新2指针，将该位置赋值到2指针处
            # 暂时不更新迭代器，因为更新值后还有可能是1，需要再等一次
            else:
                two_ptr -= 1
                nums[i], nums[two_ptr] = nums[two_ptr], nums[i]



nums = [2, 0, 2, 1, 1, 0]
solution = Solution()
solution.sortColors(nums)
print(nums)
