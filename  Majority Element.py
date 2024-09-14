# Problem statement
# You are given an array 'a' of 'n' integers.

# A majority element in the array ‘a’ is an element that appears more than 'n' / 2 times.

# Find the majority element of the array.

# It is guaranteed that the array 'a' always has a majority element.

# Example:
# Input: ‘n’ = 9, ‘a’ = [2, 2, 1, 3, 1, 1, 3, 1, 1]

# Output: 1

# Explanation: The frequency of ‘1’ is 5, which is greater than 9 / 2.
# Hence ‘1’ is the majority element.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 9
# 2 2 1 3 1 1 3 1 1

# Sample Output 1:
# 1

# Explanation Of Sample Input 1:
# Input: ‘n’ = 9, ‘a’ = [2, 2, 1, 3, 1, 1, 3, 1, 1]

# Output: 1

# Explanation: The frequency of ‘1’ is 5, which is greater than 9 / 2.
# Hence ‘1’ is the majority element.

# Sample Input 2:
# 1
# 4

# Sample Output 2:
# 4

# Sample Input 3:
# 5
# -53 75 56 56 56 

# Sample Output 3:
# 56

# Expected time complexity :
# The expected time complexity is O(n).

# Constraints :
# 1 <= 'n' <= 10000
# 0 <= 'arr[i]' <= 10^9



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ele = None
        for i in range(0,len(nums)):
            if cnt == 0:
                cnt = 1
                ele = nums[i]
            elif nums[i] == ele:
                cnt +=1
            else:
                cnt -=1
        return ele
    
    def majorityElement(v: [int]) -> int:
    hashMap = {}
    for i in v:
        if i in hashMap:
            hashMap[i]+=1
        else:
            hashMap[i]=1
    half = len(v)//2
    for i in hashMap:
        if hashMap[i]>half:
            return i