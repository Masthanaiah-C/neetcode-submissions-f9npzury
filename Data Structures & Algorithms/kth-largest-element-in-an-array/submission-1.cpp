class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::map<int, int> m;
        std::priority_queue<pair<int,int>> pq;

        for (auto num:nums){
            m[num]++; 
        }

        for (const auto &pair : m) {
            pq.push(pair);
        }

        while(k){
            auto p = pq.top();
            k = k - p.second;
            if (k <= 0) return p.first;
            pq.pop();
        }
    return -1;
    }
};
