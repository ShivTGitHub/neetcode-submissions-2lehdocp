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
        // if(!root){return nullptr;}
        int ip= p->val;
        int iq= q->val;
        while(root){
            cout<<root->val<<endl;
            if(root->val > ip && root->val > iq){ root=root->left;}
            else if(root->val < ip && root->val < iq){root=root->right;}
            else{return root;}
        }
        return root;
    }
};
