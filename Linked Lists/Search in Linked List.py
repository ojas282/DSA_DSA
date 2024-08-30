# Given a linked list of n nodes and a key , the task is to check if the key is present in the linked list or not.

# Example:

# Input:
# n = 4
# 1->2->3->4
# Key = 3
# Output:
# True
# Explanation:
# 3 is present in Linked List, so the function returns true.
# Your Task:
# Your task is to complete the given function searchKey(), which takes a head reference and key as Input and returns true or false boolean value by checking the key is present or not in the linked list.

# Constraint:
# 1 <= n <= 105
# 1 <= key <= 105

# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

#User function Template for python3


''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        curr = head
        while curr is not None:
            if curr.data == key:
                return True
            curr  = curr.next
        return False
            

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        data = list(map(int, input().strip().split()))
        head = Node(data[0])
        tail = head
        for i in range(1, n):
            tail.next = Node(data[i])
            tail = tail.next
        key = int(input())
        ob = Solution()
        res = ob.searchKey(n, head, key)
        key = 0
        if res == True:
            key = 1
        print(key)

# } Driver Code Ends
