class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int length = arr.size();
        int maxtoRight = -1;
        for (int i = length - 1; i>=0 ; i--) {
            
            if (i == length - 1) {
                maxtoRight = max(maxtoRight, arr[i]);
                arr[i] = -1;
                continue;
            }
            int temp = arr[i];
            arr[i] = maxtoRight;
            maxtoRight = max(maxtoRight, temp);
        }
        return arr;
    }
};