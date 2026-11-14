class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        // A should always be the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size();
        int n = nums2.size();

        int total = m + n;
        int half = (total + 1) / 2;

        int low = 0;
        int high = m;

        while (low <= high) {

            // Number of elements taken from nums1
            int i = low + (high - low) / 2;

            // Number of elements taken from nums2
            int j = half - i;

            int Aleft = (i == 0) ? INT_MIN : nums1[i - 1];
            int Aright = (i == m) ? INT_MAX : nums1[i];

            int Bleft = (j == 0) ? INT_MIN : nums2[j - 1];
            int Bright = (j == n) ? INT_MAX : nums2[j];

            // nums1 partition is too far right
            if (Aleft > Bright) {
                high = i - 1;
            }

            // nums1 partition is too far left
            else if (Bleft > Aright) {
                low = i + 1;
            }

            // Correct partition found
            else {

                // Odd number of elements
                if (total % 2 == 1) {
                    return max(Aleft, Bleft);
                }

                // Even number of elements
                int leftMax = max(Aleft, Bleft);
                int rightMin = min(Aright, Bright);

                return ((double)leftMax + rightMin) / 2.0;
            }
        }

        return 0.0; // Should never reach here for valid input
    }
};