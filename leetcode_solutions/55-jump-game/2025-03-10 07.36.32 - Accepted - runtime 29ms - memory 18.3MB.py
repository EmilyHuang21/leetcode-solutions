class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Track the farthest index we can reach
        
        for i in range(len(nums)):
            if i > max_reach:  # If we can't reach index i, return False
                return False
            
            max_reach = max(max_reach, i + nums[i])  # Update max reach
            
            if max_reach >= len(nums) - 1:  # If we can reach the last index, return True
                return True
        
        return False