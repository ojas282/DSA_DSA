# Geek is learning data structures and is familiar with linked lists, but he's curious about how to access the previous element in a linked list in the same way that we access the next element. His teacher explains doubly linked lists to him.

# Given an integer array arr of size n. Construct the doubly linked list from arr and return the head of it.

# Example 1:

# Input:
# n = 5
# arr = [1,2,3,4,5]
# Output:
# 1 2 3 4 5
# Explanation: Linked list for the given array will be 1<->2<->3<->4<->5.
# Example 2:

# Input:
# n = 1
# arr = [1]
# Output:
# 1
# Explanation: Linked list for the given array will be 1.
# Constraints:
# 1 <= n <= 105
# 1 <= arr[i] <= 100

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function constructDLL() which takes arr[] as input parameters and returns the head of the Linked List.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

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
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        if not arr:
            return 0
        else:
            head = Node(arr[0])
            curr = head
            
            for i in range(1,len(arr)):
                new_node = Node(arr[i])
                curr.next = new_node
                new_node.prev = curr
                curr = new_node
        return head
                

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
    
def printList(node):
    tmp = node
    if tmp:
        c1, c2 = 0, 0
        while tmp.next:
            c1 += 1
            tmp = tmp.next
        while tmp.prev:
            c2 += 1
            tmp = tmp.prev
        if c1 != c2:
            print("-1")
            return
    while tmp:
        print(tmp.data, end = " ")
        tmp = tmp.next
    print()

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructDLL(arr)
        printList(res)
# } Driver Code Ends