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
#include <stack>
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        // Base Case
        vector<int> inOrder;
        if (root == NULL)
        {
            return inOrder;
        }
        if (root->left == NULL && root->right == NULL) {
            inOrder.push_back(root->val);
            return inOrder;
        }
         
        // Get left skewed Tree
        stack<TreeNode*> myLeftTree;
        TreeNode* leftNode = root;
        while (leftNode != NULL) {
            myLeftTree.push(leftNode);
            leftNode = leftNode->left;
        }
        
        //Start popping the elements

        while(!myLeftTree.empty()) {
            TreeNode* node = myLeftTree.top();
            myLeftTree.pop();
            inOrder.push_back(node->val);
            if (node->right != NULL) {
                
                TreeNode* rightNode = node->right;
                while (rightNode != NULL) {
                    myLeftTree.push(rightNode);
                    rightNode = rightNode->left;
                }
            }
        }
        return inOrder;
    }
};