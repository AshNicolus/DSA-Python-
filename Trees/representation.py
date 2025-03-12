class Treenode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right =None
def CreateNode(root,l):
    if not root or  len(l)!=7:
        return
    root.left =Treenode(l[0])
    root.right = Treenode(l[1])
    root.left.left=Treenode(l[3])
    root.left.right= Treenode(l[4])
    root.right.left =Treenode(l[5])
    root.right.right = Treenode(l[6])


def print(root):
    if not root:
        return
    queue= [root]
    while queue:
        node = queue.pop(0)
        print(node.data,end=" ")


        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)