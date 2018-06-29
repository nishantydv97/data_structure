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

def main():
    tree=bst()
    tr=tree.create_node(0)
    tree.insert_node(tr,15)
    tree.insert_node(tr,10)
    tree.insert_node(tr,20)
    tree.insert_node(tr,25)
    tree.insert_node(tr,8)
    tree.insert_node(tr,12)
#    print(tr.right.left.right.data)
    print("postorder traversal of the above tree is ")
    tree.post_display(tr)
    print("\n")
    print("preorder traversal of the above tree is ")
    tree.preorder_display(tr)
    print("\n")
    print("inorder traversal of the above tree is ")
    tree.inorder_display(tr)
    print("\n")


if __name__ == '__main__':
    main()
