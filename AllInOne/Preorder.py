from collections import deque

def Preorder(root) :
    
    visited = []

    
    current_node = root
    if current_node not in visited :
        visited.append(current_node.value)
    if current_node.left :
        Preorder(current_node.left)
    if current_node.right :
        Preorder(current_node.right)

    return visited        