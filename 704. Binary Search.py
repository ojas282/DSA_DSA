# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

#iterative approach
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while(low<=high):
            mid = (low+high)//2

            if nums[mid]==target:
                return mid
            elif target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
        return -1

#using recurssion  
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
    
    def binarySearch(self, nums: List[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2 
        if nums[mid] == target: 
            return mid
        elif target > nums[mid]:
            return self.binarySearch(nums, mid + 1, high, target)
        else:
            return self.binarySearch(nums, low, mid - 1, target)
