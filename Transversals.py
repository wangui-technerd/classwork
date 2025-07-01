class TreeNode:
    def __init__(self,value):

        self.left=None
        self.right=None
        self.value=value

    def insert(self,key):

        if key<self.value:
            if self.left is None:
                self.left=TreeNode(key)
            else:
                self.left.insert(key)

        elif key>self.value:
            if self.right is None:
                self.right=TreeNode(key)

            else:
                self.right.insert(key)


    def find(self,key):

        if key<self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(key)

        elif key>self.value:
            if self.right is None:
                return False

        else:
            return True



    def preorder_traversal(self):
        print(self.value)

        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()


    def postorder_traversal(self):

        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()

        print(self.value)

    def inorder_traversal(self):

        if self.left:
           self.left.inorder_traversal()

        print(self.value)

        if self.right:
            self.right.inorder_traversal()



if __name__ == "__main__":
    tree=TreeNode(50)

    tree.insert(11)
    tree.insert(12)
    tree.insert(13)
    tree.insert(14)
    #nsert("32")
    tree.insert(72)
    tree.insert(62)
    tree.insert(51)
    tree.insert(67)


    print("\n preorder_traversal: ")
    tree.preorder_traversal()

    print("\n postorder_traversal: ")
    tree.postorder_traversal()

    print("\n inorder_traversal: ")
    tree.inorder_traversal()