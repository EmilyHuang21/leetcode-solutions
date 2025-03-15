class Solution:
    def intToRoman(self, num: int) -> str:
        # 定義羅馬數字對應表（由大到小排序）
        roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        result = ""

        for value, symbol in roman_map:
            while num >= value:  # 當 `num` 大於或等於當前值時，減去對應的數值
                result += symbol
                num -= value  # 更新 `num`

        return result
            