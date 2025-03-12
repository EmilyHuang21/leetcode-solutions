class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two-pointer approach
        k=0  #Pointer for inserting non-val elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1

        return k
