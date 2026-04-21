class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        auto cap = *std::max_element(weights.begin(), weights.end());
        cout<<cap;
        for (int capacity = cap; capacity <= 500 * 50000; capacity ++ ) {
            // Simulate the shipping 
            int ships = 1;
            int shipweight = 0;
            for (auto weight: weights) {
                if (ships > days) {
                    break;
                }
                shipweight += weight;
                if (shipweight > capacity) {
                    ships++;
                    shipweight = weight;
                }
            }
            if (ships <= days) return capacity;
        }
        return cap;
    }
};