class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1  # 初始化雙指針

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # 轉換成 1-based index
            elif current_sum < target:
                left += 1  # 總和過小，左指針右移
            else:
                right -= 1  # 總和過大，右指針左移
