class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        // Iterate from the last and add 1 until you have carry as 0
        int right = digits.size() - 1;
        int carry = 0;
        do {
            int sum = digits[right] + 1;
            carry = sum/10;
            digits[right] = sum%10;
            right--;
        } while((carry == 1)&& right>=0);

        // If carry is 1, insert 1 at the begining. 
        if (carry)
           digits.insert(digits.begin()+0, 1);

        return digits;
    }
};
