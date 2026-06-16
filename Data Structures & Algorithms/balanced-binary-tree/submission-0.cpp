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

class Solution 
{
public:
    bool isBalanced(TreeNode* root)
    {
        //Recursive dfs height checking
        return checkHeight(root) != -1;
    }

private:
    int checkHeight(TreeNode* node) 
    {
        //Edge case
        if (!node)
            return 0;

        //Greatest height of left subtree
        int leftHeight = checkHeight(node->left);
        if (leftHeight == -1)
            return -1;

        //Greatest height of right subtree
        int rightHeight = checkHeight(node->right);
        if (rightHeight == -1)
            return -1; // Right side is already unbalanced, pass failure up

        //Calculate if balance valid for current node
        if (abs(leftHeight - rightHeight) > 1)
            return -1;

        return max(leftHeight, rightHeight) + 1;
    }
};
