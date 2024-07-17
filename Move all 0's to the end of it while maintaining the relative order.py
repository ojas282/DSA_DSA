# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        #storing non 0 elements in a temp array
        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
        #replacing elements in nums 
        for i in range(len(temp)):
            nums[i]=temp[i]
        #adding len(nums)-len(temp) 0's at the end of nums
        for i in range(len(temp),len(nums)):
            nums[i]=0
        return nums