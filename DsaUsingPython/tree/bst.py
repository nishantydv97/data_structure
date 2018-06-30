class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class bst:
    def create_node(self,data):
        temp=Node(data)
        return temp


    def insert_node(self,root,data):
        if root==None:
            root=self.create_node(data)
        elif(data<=root.data):
            if(root.left==None):
                root.left=self.create_node(data)
            else:
                self.insert_node(root.left,data)
        else:
            if(root.right==None):
                root.right=self.create_node(data)
            else:
                self.insert_node(root.right,data)


    def post_display(self,dnode):
        if(dnode==None):
            return
        else:
            self.post_display(dnode.left)
            self.post_display(dnode.right)
            print(dnode.data,end="->")



    def inorder_display(self,dnode):
        if(dnode==None):
            return
        else:
            self.inorder_display(dnode.left)
            print(dnode.data,end="->")
            self.inorder_display(dnode.right)


    def preorder_display(self,dnode):
        if dnode==None:
            return
        else:
            print(dnode.data,end="->")
            self.preorder_display(dnode.left)
            self.preorder_display(dnode.right)


    def bst_search(self,tree_root,data):
        if(tree_root is None):
            return(False)
        elif(tree_root.data == data):
            return (True)
        elif(data<=tree_root.data):
            return(self.bst_search(tree_root.left,data))
        else:
            return(self.bst_search(tree_root.right,data))


def main():
    tree=bst()
    tr=tree.create_node(0)
    tree.insert_node(tr,15)
    tree.insert_node(tr,10)
    tree.insert_node(tr,20)
    tree.insert_node(tr,25)
    tree.insert_node(tr,8)
    tree.insert_node(tr,12)

    print("postorder traversal of the above tree is ")
    tree.post_display(tr)
    print("\n")

    print("preorder traversal of the above tree is ")
    tree.preorder_display(tr)
    print("\n")

    print("inorder traversal of the above tree is ")
    tree.inorder_display(tr)
    print("\n")

    z=tree.bst_search(tr,12)
    if(z):
        print("number 12 found in the tree ")
    else:
        print("number 12 not found in the tree ")
#    print("\n")
    z=tree.bst_search(tr,145)
    if(z):
        print("number 145 found in the tree ")
    else:
        print("number 145 not found in the tree ")


if __name__ == '__main__':
    main()
