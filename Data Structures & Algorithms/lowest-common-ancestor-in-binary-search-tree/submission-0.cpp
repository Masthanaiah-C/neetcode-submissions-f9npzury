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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        //Base Case - One of them is Node
        if (root->val == p->val || root->val == q->val) {
            return root;
        }
        int smaller,bigger;
        if (p->val < q->val) {
            smaller = p->val;
            bigger = q->val;
        } else {
            bigger = p->val;
            smaller = q->val;
        }

        if(root->val >= smaller && root->val <= bigger) {
            return root;
        } else if (root->val < smaller && root->val < bigger) {
            return lowestCommonAncestor(root->right, p, q);
        } else {
            return lowestCommonAncestor(root->left, p, q);
        }
    
    }
};
