from collections import deque

def Preorder(root) :
    
    visited = []

    q = deque()
    q.append(root)

    while q :
        current_node = q.popleft()
        visited.append(current_node)

        if current_node.left :
            Preorder(current_node.left)
        if current_node.right :
            Preorder(current_node.right)

    return visited        