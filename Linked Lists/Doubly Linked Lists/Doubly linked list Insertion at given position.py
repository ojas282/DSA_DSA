# Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list.

# Example 1:

# Input:
# LinkedList: 2<->4<->5
# p = 2, x = 6 
# Output: 2 4 5 6
# Explanation: p = 2, and x = 6. So, 6 is
# inserted after p, i.e, at position 3
# (0-based indexing).
# Example 2:

# Input:
# LinkedList: 1<->2<->3<->4
# p = 0, x = 44
# Output: 1 44 2 3 4
# Explanation: p = 0, and x = 44 . So, 44
# is inserted after p, i.e, at position 1
# (0-based indexing).
# Your Task:
# The task is to complete the function addNode() which head reference, position and data to be inserted as the arguments, with no return type.

# Expected Time Complexity : O(N)
# Expected Auxilliary Space : O(1)

# Constraints:
# 1 <= N <= 104
# 0 <= p < N

# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''
#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    curr = head
    new_node = Node(data)
    if curr is None:
        head = new_node
        return head
    for i in range(p):
        curr = curr.next
    
    if curr.next is None:
        curr.next = new_node
        new_node.prev = curr
        new_node.next = None
    else:
        new_node.next = curr.next
        curr.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr
        
    
    

    
        
        



#{ 
 # Driver Code Starts
class Node:
	def __init__(self, data):
		self.data = data
		
		
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, new_data):
		new_node = Node(new_data)
		if(self.head == None):
		    self.head = new_node
		    self.tail = new_node
		    return
		
		self.tail.next = new_node
		new_node.prev = self.tail
		self.tail = new_node
		return
		
	def printList(self, node):
		while(node.next is not None):
			node = node.next
		while node.prev is not None:
		    node = node.prev
		while(node is not None):
		    print(node.data, end=" ")
		    node = node.next
		print()
		
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = map(int, input().strip().split())
        llist = DoublyLinkedList()
        for e in arr:
            llist.add(e)
            
        pos,data = map(int, input().strip().split())
        
        addNode(llist.head, pos, data)
        llist.printList(llist.head)

# } Driver Code Ends