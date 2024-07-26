# Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

# Example 1:

# Input: 
# n = 5, arr1[] = {1, 2, 3, 4, 5}  
# m = 5, arr2 [] = {1, 2, 3, 6, 7}
# Output: 
# 1 2 3 4 5 6 7
# Explanation: 
# Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
# Example 2:

# Input: 
# n = 5, arr1[] = {2, 2, 3, 4, 5}  
# m = 5, arr2[] = {1, 1, 2, 3, 4}
# Output: 
# 1 2 3 4 5
# Explanation: 
# Distinct elements including both the arrays are: 1 2 3 4 5.
# Example 3:

# Input:
# n = 5, arr1[] = {1, 1, 1, 1, 1}
# m = 5, arr2[] = {2, 2, 2, 2, 2}
# Output: 
# 1 2
# Explanation: 
# Distinct elements including both the arrays are: 1 2.
# Your Task: 
# You do not need to read input or print anything. Complete the function findUnion() that takes two arrays arr1[], arr2[], and their size n and m as input parameters and returns a list containing the union of the two arrays.

# Expected Time Complexity: O(n+m).
# Expected Auxiliary Space: O(n+m).

# Constraints:
# 1 <= n, m <= 105
# -109 <= arr1[i], arr2[i] <= 109

#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        #using 2 pointers approach
        i = j = 0
        union = []
        while (i<n and j <m):
            if arr1[i]<=arr2[j]:
                if len(union)==0 or union[-1]!=arr1[i]:
                    union.append(arr1[i])
                i+=1
            else:
                if len(union)==0 or union[-1]!=arr2[j]:
                    union.append(arr2[j])
                j+=1
                
        while (i<n):
            if union[-1]!=arr1[i]:
                union.append(arr1[i])
            i+=1
        while (j<m):
            if union[-1]!=arr2[j]:
                union.append(arr2[j])
            j+=1
        return union
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends