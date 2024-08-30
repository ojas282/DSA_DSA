# Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.

# Examples :

# Input: LinkedList: 1->2->3->4->5 , x = 6
# Output: 1->2->3->4->5->6
# Explanation: 

# We can see that 6 is inserted at the end of the linkedlist.
# Input: LinkedList: 5->4 , x = 1
# Output: 5->4->1
# Explanation: 

# We can see that 1 is inserted at the end of the linkedlist.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 0 <= number of nodes <= 105
# 1 <= node->data , x <= 103

'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        new_node = Node(x)
        if head is None:
            return new_node
        i = head
        while i.next is not None:
            i = i.next
        i.next = new_node
        return head




#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))
        x = int(data[idx + 1].strip())
        idx += 2

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        ob = Solution()
        ans = ob.insertAtEnd(head, x)
        printList(ans)

        t -= 1

# } Driver Code Ends