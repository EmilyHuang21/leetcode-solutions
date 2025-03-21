class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)

        # Step 1: Remove '_' and check order of L and R
        s_filtered = [(c, i) for i, c in enumerate(start) if c != '_']
        t_filtered = [(c, i) for i, c in enumerate(target) if c != '_']

        if len(s_filtered) != len(t_filtered) or [c for c, _ in s_filtered] != [c for c, _ in t_filtered]:
            return False

        # Step 2: Compare Positions
        for (c1, i1), (c2, i2) in zip(s_filtered, t_filtered):
            if c1 == 'L' and i1 < i2:  # 'L' must move left
                return False
            if c1 == 'R' and i1 > i2:  # 'R' must move right
                return False

        return True
        