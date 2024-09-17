# Given an array arr of n positive integers, your task is to find all the leaders in the array. An element of the array is considered a leader if it is greater than all the elements on its right side or if it is equal to the maximum element on its right side. The rightmost element is always a leader.

# Examples

# Input: n = 6, arr[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.
# Input: n = 5, arr[] = {10,4,2,4,1}
# Output: 10 4 4 1
# Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side
# Input: n = 4, arr[] = {5, 10, 20, 40} 
# Output: 40
# Explanation: When an array is sorted in increasing order, only the rightmost element is leader.
# Input: n = 4, arr[] = {30, 10, 10, 5} 
# Output: 30 10 10 5
# Explanation: When an array is sorted in non-increasing order, all elements are leaders.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 <= n <= 107
# 0 <= arr[i] <= 107

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        ans=[]
        maxi = float('-inf')
        for i in range(n-1,-1,-1):
            if arr[i]>=maxi:
                maxi = arr[i]
                ans.append(maxi)
        # reversing      
        low = 0
        high = len(ans)-1
        while low < high:
            ans[low],ans[high] = ans[high],ans[low]
            low+=1
            high-=1
            
        return ans
        
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends