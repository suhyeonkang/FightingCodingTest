
def LCA(root, p, q):

    if root is None:
        return None
    
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if left == None and right == None :
        return None
    elif left or right :
        return root
    elif root == p or root == q :
        return root 
