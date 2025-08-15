class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if(root == nullptr) {
            return result;
        }
        queue<TreeNode*> queue;
        queue.push(root);
        while(!queue.empty()) {
            vector<int> vect;
            int queueSize = queue.size();
            for(int i = 0; i < queueSize; i++) {
                TreeNode* temp = queue.front();
                vect.push_back(temp->val);
                queue.pop();
                if(temp->left != nullptr) {
                    queue.push(temp->left);
                }
                if(temp->right != nullptr) {
                    queue.push(temp->right);
                }
            }
            result.push_back(vect);
        }
        return result;
    }
};