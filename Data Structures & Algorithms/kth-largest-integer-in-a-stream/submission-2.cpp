class KthLargest {
public:
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
    int gK;
    KthLargest(int k, vector<int>& nums) {
        for (auto num: nums) pq.push(num);
        while(pq.size() > k) pq.pop();
        gK = k;

    }
    
    int add(int val) {
        pq.push(val);
        if (pq.size()>gK)
        pq.pop();
        cout<<pq.size();
        return pq.top();
        
    }
};
