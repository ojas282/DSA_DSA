# Given an array of integer arr. Your task is to construct the linked list from arr & return the head of the linked list.

# Examples:

# Input: arr = [1, 2, 3, 4, 5]
# Output: LinkedList: 1->2->3->4->5
# Explanation: Linked list for the given array will be

# Input: arr = [2, 4, 6, 7, 5, 1, 0]
# Output: LinkedList: 2->4->6->7->5->1->0
# Explanation: Linked list for the given array will be

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 <= arr.size() <= 106
# 1 <= arr[i] <= 106

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    def constructLL(self, arr):
        if not arr:
            return None
        
        head = Node(arr[0])
        curr = head
        
        for value in arr[1:]:
            curr.next = Node(value)
            curr = curr.next
        return head
            
        # code here


#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        # n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
# } Driver Code Ends