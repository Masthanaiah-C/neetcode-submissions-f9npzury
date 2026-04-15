/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isBalancedTree = true;
    int height(TreeNode* node) {
        if (node == nullptr) return 0;
        if (node->left == nullptr && node->right == nullptr) return 1;
        int leftHeight = 1 + height(node->left);
        int rightHeight = 1 + height(node->right);
        if (abs(leftHeight - rightHeight) > 1) isBalancedTree = false;
        return max(leftHeight, rightHeight);
    }
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) return true;
        height(root);
        return isBalancedTree;
    }
};
