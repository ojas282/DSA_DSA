# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

# Examples:

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.
# Input: arr[] = [90, 80, 100, 70, 40, 30]
# Output: false
# Explanation: The given array is not sorted.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ arr.size ≤ 106
# - 109 ≤ arr[i] ≤ 109

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        n=len(arr)
        if n==0 or n==1:
            return True
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                return False
        return True


#{ 
 # Driver Code Starts
# Importing necessary modules
import sys
from typing import List

# Main function
if __name__ == "__main__":
    input = sys.stdin.read().strip().split("\n")
    t = int(input[0])
    index = 1
    solution = Solution()

    for _ in range(t):
        line = list(map(int, input[index].strip().split()))
        index += 1
        ans = solution.arraySortedOrNot(line)
        print("true" if ans else "false")
# } Driver Code Ends