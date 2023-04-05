from collections import deque

def Indorder(root):
    
    visited = []

    if root is None :
        return 0

    current_node = root
    if current_node.left not in visited :
        Indorder(current_node.left)
    if current_node not in visited :
        visited.append(current_node.value)    
    if current_node.right :
        Indorder(current_node.right)

    return visited    
