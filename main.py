class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        
        # Start with the root node
        leftmost = root
        
        while leftmost.left:  # Traverse levels
            # Go through the current level
            head = leftmost
            while head:  # Traverse nodes at the current level
                # Connect left and right children
                head.left.next = head.right
                
                # Connect right child to the next left child
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node
                head = head.next
            
            # Move to the next level
            leftmost = leftmost.left
        
        return root

# Example usage:
# Constructing the perfect binary tree: [1,2,3,4,5,6,7]
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()
solution.connect(root)

# Output the next pointers
def print_next_pointers(node):
    while node:
        print(node.val, "->", node.next.val if node.next else "None", end=' ')
        node = node.next

print_next_pointers(root)        # Level 1
print_next_pointers(root.left)   # Level 2
print_next_pointers(root.left.left)  # Level 3
