class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []  # This will store unique triplets
        n = len(nums)

        for i in range(n - 2):  # Traverse the list, fixing one number at a time
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            
            left, right = i + 1, n - 1  # Two-pointer approach
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Compute sum of triplet
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])  # Valid triplet found
                    # Move left and right pointers to skip duplicate values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # Increase left pointer to get a larger sum
                else:
                    right -= 1  # Decrease right pointer to get a smaller sum

        return result  # Return all unique triplets