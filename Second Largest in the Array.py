.#User function Template for python3
# Given an array arr, return the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

# Examples:

# Input: arr = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr = [10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist so answer is -1.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arri ≤ 105


class Solution:
    def print2largest(self, arr):
        #Brute Solution
        # arr1=sorted(arr)
        # slargest = -1
        # largest = arr1[-1]
        # for i in range(len(arr1)-1,-1,-1):
        #     if arr1[i]==largest:
        #         continue
        #     else:
        #         slargest = arr1[i]
        #         break
        # return slargest
        #Time Taken : 0.62
        
        
        #Better Solution
        # largest = arr[0]
        # for i in range(len(arr)):
        #     if arr[i]>largest:
        #         largest = arr[i]
        # second_largest = -1
        # for i in range(len(arr)):
        #     if arr[i]>second_largest and arr[i]!=largest:
        #         second_largest = arr[i]
        # return second_largest
        #Time Taken : 0.43
        
        
        #Optimal Solution
        # largest = arr[0]
        # second_largest = -1
        # for i in range(len(arr)):
        #     if arr[i]>largest:
        #         second_largest = largest
        #         largest = arr[i]
        #     elif arr[i]<largest and arr[i]>second_largest:
        #         second_largest = arr[i]
        # return second_largest
        #Time Taken : 0.45
        
        
        
            
                

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends