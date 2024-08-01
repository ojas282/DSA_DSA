# Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

 

# Examples:
 

# Input :
# arr[] = {10, 5, 2, 7, 1, 9}, k = 15
# Output : 4
# Explanation:
# The sub-array is {5, 2, 7, 1}.
# Input : 
# arr[] = {-1, 2, 3}, k = 6
# Output : 0
# Explanation: 
# There is no such sub-array with sum 6.
# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(n).

 

# Constraints:
# 1<=n<=105
# -105<=arr[i], K<=105

#User function Template for python3

#approach 1 using a hashmap

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        
        prefix_sum = 0
        max_len = 0
        hashmap ={}
        
        for i in range(n):
            prefix_sum+=arr[i]
            
            if prefix_sum ==k:
                max_len = i+1
            
            if prefix_sum-k in hashmap:
                max_len = max(max_len, i - hashmap[prefix_sum-k])
            
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i
        return max_len
                
                






#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends