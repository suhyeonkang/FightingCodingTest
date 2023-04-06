from collections import deque

def Postorder(root):

    visited=[]

    current_node = root
    if current_node.left :
        Postorder(current_node.left)
    if current_node.right :
            Postorder(current_node.right)
    if current_node not in visited :
            visited.append(current_node.value)


    return visited                    