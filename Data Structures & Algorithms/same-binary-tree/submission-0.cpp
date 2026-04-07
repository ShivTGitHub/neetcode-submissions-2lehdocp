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
    // bool comp(TreeNode* t, TreeNode* r){
    //     if(!t && !r){return true;}
    //     if(t->val == r->val){
    //         return (t->left, r->left) && (t->right, r->right);
    //     }
    //     return false;
    // }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q){return true;}
        if(!p || !q){return false;}
        if(p->val!=q->val){return false;}
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}
};
