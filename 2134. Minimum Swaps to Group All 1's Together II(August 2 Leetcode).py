# A swap is defined as taking two distinct positions in an array and swapping the values in them.

# A circular array is defined as an array where we consider the first element and the last element to be adjacent.

# Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 

# Example 1:

# Input: nums = [0,1,0,1,1,0,0]
# Output: 1
# Explanation: Here are a few of the ways to group all the 1's together:
# [0,0,1,1,1,0,0] using 1 swap.
# [0,1,1,1,0,0,0] using 1 swap.
# [1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
# There is no way to group all 1's together with 0 swaps.
# Thus, the minimum number of swaps required is 1.
# Example 2:

# Input: nums = [0,1,1,1,0,0,1,1,0]
# Output: 2
# Explanation: Here are a few of the ways to group all the 1's together:
# [1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
# [1,1,1,1,1,0,0,0,0] using 2 swaps.
# There is no way to group all 1's together with 0 or 1 swaps.
# Thus, the minimum number of swaps required is 2.
# Example 3:

# Input: nums = [1,1,0,0,1]
# Output: 0
# Explanation: All the 1's are already grouped together due to the circular property of the array.
# Thus, the minimum number of swaps required is 0.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count_1s = 0
        count_0s = 0
        size = len(nums)
        #counting number of 1's
        for i in nums:
            if i == 1:
                count_1s += 1

        window_size = count_1s
        
        #runngin a loop in the window 
        for i in range(window_size):
            if nums[i] == 0:
                count_0s += 1

        #calculating least number of swaps required for each window to replace 0s with 1s
        least = count_0s

        for i in range(window_size,window_size+ size):
            #check if the upcoming element in the window is 0 or not is yes then raise count0s value
            if nums[i%size]==0:
                count_0s += 1
            #check if the leaving element in the window is 0 or not if yes the decrement count0s value by 1
            if nums[i-window_size]==0:
                count_0s -=1
                
            #calculate the least number of swaps 
            least=min(least,count_0s)
            
        return least