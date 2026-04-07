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
    bool same(TreeNode* p, TreeNode* q){
        if(!p && !q){return true;}
        // if(p && !q){return true;}
        if(!p || !q){return false;}
        // cout<<p->val<<", "<<q->val<<endl;
        if(p->val != q->val){return false;}
        return same(p->left, q->left) && same(p->right, q->right);
    }
    bool res=false;
    // bool res;
    void dfs(TreeNode* rt, TreeNode* srt){
        if(!rt){/*cout<</*"null"<<endl*/; return;}
        // cout<<rt->val<<endl;
        if(rt->val==srt->val){res=res || same(rt, srt);}
        // cout<<res<<endl;
        if(res==true){cout<<"same"<<endl; return;}
        dfs(rt->left, srt);
        dfs(rt->right, srt);

    }
    bool isSubtree(TreeNode* rt, TreeNode* srt) {
        // return same(rt->left, srt);
        // bool res;
        dfs(rt, srt);
        return res;

    }
};


//1,null,1,null,1,null,1,null,1,null,1,2]
//1,null,1,null,1,null,1,null,1,null,1,2]
//[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]
//                                   ,1,null,1,null,1,null,1,null,1,null,1,2]