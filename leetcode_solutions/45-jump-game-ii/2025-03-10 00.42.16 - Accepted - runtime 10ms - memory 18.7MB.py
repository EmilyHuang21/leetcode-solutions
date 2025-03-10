class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0  # Already at the last index
        
        jumps = 0
        max_reach = 0
        end_of_current_jump = 0

        for i in range(n - 1):  # We don't need to check last index
            max_reach = max(max_reach, i + nums[i])  # Update max reach
            
            if i == end_of_current_jump:  # Need to jump
                jumps += 1
                end_of_current_jump = max_reach
                
                if end_of_current_jump >= n - 1:  # If we can reach last index, break early
                    break
        
        return jumps