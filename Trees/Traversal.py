class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    inorder_list=[]
    preorder_list=[]
    postorder_list=[]
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        inorder_list.append(root.data)
        inorder(root.right)
    def preorder(root):
        if not root:
            return
        preorder_list.append(root.data)
        preorder(root.left)
        preorder(root.right)
    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        postorder_list.append(root.data)
    inorder(root)
    preorder(root)
    postorder(root)
    return [inorder_list,preorder_list,postorder_list]