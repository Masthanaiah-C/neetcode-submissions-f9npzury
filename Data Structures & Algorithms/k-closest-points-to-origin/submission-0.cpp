class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> p;
        std::priority_queue<pair <double, vector<int> >, vector<pair<double, vector<int> >>, std::greater<pair<double, vector<int>>>> pq;
        for (auto point: points) {
            double distance = (point[0]*point[0]) + (point[1]*point[1]);
            pq.push({distance, point});
        }
        while(k--) {
            auto pnt = pq.top();
            p.push_back(pnt.second);
            pq.pop();
        }
        
        return p;
    }
};
