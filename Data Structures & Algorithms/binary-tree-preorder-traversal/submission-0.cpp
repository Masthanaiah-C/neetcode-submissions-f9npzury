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
    vector<int> order;
    TreeNode* saveRoot = nullptr;
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == nullptr) return order;
        if (saveRoot == nullptr) saveRoot=root;
        order.push_back(root->val);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
        if (saveRoot == root) return order;
        return order;

    }
};