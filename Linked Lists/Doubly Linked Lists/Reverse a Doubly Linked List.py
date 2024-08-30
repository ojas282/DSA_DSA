# Given a doubly linked list. Your task is to reverse the doubly linked list and return its head.

# Examples:

# Input: LinkedList: 3 <-> 4 <-> 5
# Output: 5 <-> 4 <-> 3

# Input: LinkedList: 75 <-> 122 <-> 59 <-> 196
# Output: 196 <-> 59 <-> 122 <-> 75

# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= number of nodes <= 106
# 0 <= node->data <= 104

#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        curr = head
        arr=[]
        while curr is not None:
            arr.append(curr.data)
            curr = curr.next
        curr = head
        length = len(arr)
        for i in range(length):
            curr.data = arr[(len(arr)-1)-i]
            curr = curr.next
            
        return head
            
            
            



#{ 
 # Driver Code Starts
class DLLNode:

    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def push(tail, new_data):
    newNode = DLLNode(new_data)
    newNode.next = None
    newNode.prev = tail

    if tail:
        tail.next = newNode

    return newNode


def printList(head):
    if not head:
        return

    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = DLLNode(arr[0])
        tail = head

        for value in arr[1:]:
            tail = push(tail, value)

        ob = Solution()
        resHead = ob.reverseDLL(head)
        printList(resHead)

# } Driver Code Ends