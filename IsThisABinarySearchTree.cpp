// The problem is here:
// https://www.hackerrank.com/challenges/ctci-is-binary-search-tree

bool checkRange(Node* root, int min, int max){
	if(root == NULL)
		return true;
	else 
		return min < root->data and root->data < max
			and checkRange(root->left, min, root->data)
			and checkRange(root->right, root->data, max);
}

bool checkBST(Node* root) {
	return checkRange(root, 0, 10001);
}

