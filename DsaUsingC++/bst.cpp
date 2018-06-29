#include<bits/stdc++.h>
using namespace std;
class node{
public:
	int data;
	node * left=NULL;
	node * right =NULL;
};
class bst{
public:
	node * insert(node * root,int data);
	bool search(node * root,int data);
	node * create_node(int data);
	node * delete_node(node * root,int data);
	void inorder_display(node * root);
	void postorder_display(node * root);
	void preorder_display(node * root);
};
node * bst :: insert(node * root,int data){
	if(root==NULL){
		root=create_node(data);
		return root;
	}
	else if(root->data>=data){
		root->left=insert(root->left,data);
	}
	else{
		root->right=insert(root->right,data);
	}
	return root;
}
node * bst :: create_node(int data){
	node * temp=new node();
	temp->data=data;
	return temp;
}
void bst :: preorder_display(node * root){
	if(root==NULL){
		return;
	}
	cout<<root->data<<"->";
	inorder_display(root->left);
	inorder_display(root->right);

}
void bst :: inorder_display(node * root){
	if(root==NULL){
		return;
	}
	inorder_display(root->left);
	cout<<root->data<<"->";
	inorder_display(root->right);

}

void bst :: postorder_display(struct node* node)
{
     if (node == NULL)
        return;
     postorder_display(node->left);
     postorder_display(node->right);
     printf("%d->", node->data);
}
int main(){
	node *root=new node();
	bst b;
	b.insert(root,15);
	b.insert(root,10);
	b.insert(root,20);
	b.insert(root,25);
	b.insert(root,8);
	b.insert(root,12);
	b.inorder_display(root);
	cout<<"\n";
	b.postorder_display(root);
	cout<<"\n";
	b.preorder_display(root);
	cout<<"\n";
	b.inorder_display(root);
	cout<<"\n";
	return 0;
}

