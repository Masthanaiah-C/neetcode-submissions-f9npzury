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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        //Base Condition - No Root
        if (root == NULL) {
            root = new TreeNode(val);
            return root;
        }

        //Traverse the tree until the location is found to be placed
        TreeNode* parentNode = root;
        
        while(true) {
            if (parentNode->val < val) {
                if (parentNode->right == NULL) {
                    parentNode->right = new TreeNode(val);
                    break;
                }
                else {
                    parentNode = parentNode -> right;
                }
            } else {
                if (parentNode->left == NULL) {
                    parentNode->left = new TreeNode(val);
                    break;
                }
                else {
                    parentNode = parentNode -> left;
                }
            }
        }
        return root;
    }
};