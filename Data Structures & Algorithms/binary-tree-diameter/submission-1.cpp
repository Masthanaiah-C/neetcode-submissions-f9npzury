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
    int diameter = 0;
    TreeNode* initial = NULL;
    int diameterOfBinaryTree(TreeNode* root) {
        if (initial == NULL) {
            initial = root;
        }
        if (root == NULL) {
            return 0;
        }
        if ((root->left == NULL )&& (root->right ==NULL)) {
            if (root==initial) return 0;
            return 1;
        }
        int maxLeftDepth = 0;
        int maxRightDepth = 0;


        maxLeftDepth =  diameterOfBinaryTree(root->left);
        maxRightDepth = diameterOfBinaryTree(root->right);
        diameter = max(diameter, maxLeftDepth+maxRightDepth);
        if(initial == root) {
            return diameter;
        }

        return max(1+ maxLeftDepth,1+maxRightDepth);
    }
};
