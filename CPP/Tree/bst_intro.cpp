#include<iostream>

class TreeNode {
    public:
        int key;
        char val;
        TreeNode *left;
        TreeNode *right;

        TreeNode(int key, int val): key(key), val(val), left(nullptr), right(nullptr){}

        bool operator==(const TreeNode& other) const{
            return key == other.key;
        }
        bool operator<(const TreeNode& other) const{
            return key < other.key;
        }
};

class BinarySearchTree {
    private:
        TreeNode *root;

        TreeNode* put(TreeNode* node, int key, char val){
            if (node == nullptr) return new TreeNode(key, val);
            if (key == node->key){
                node->val = val;
            } else if (key < node->key) {
                node->left = put(node->left, key, val);
            } else {
                node->right = put(node->right, key, val);
            }
            return node;
        }
        void inorder(TreeNode * node){
            if (node == nullptr) return;
            if (node->left != nullptr)
                inorder(node->left);
            std::cout << node->key << " " << node->val << std::endl;
            if (node->right != nullptr)
                inorder(node->right);
        }
    public:
        TreeNode* put(int key, char val){
            root = put(root, key, val);
            return root;
        }
        void inorder(){
            inorder(root);
        }
};

int main(){
    BinarySearchTree bst;
    bst.put(10, 'A');
    bst.put(5, 'B');
    bst.put(15, 'C');
    bst.put(2, 'D');
    bst.put(7, 'E');
    bst.put(12, 'F');
    bst.put(17, 'G');
    bst.put(2, 'Z');
    bst.inorder();
    return 0;
}
