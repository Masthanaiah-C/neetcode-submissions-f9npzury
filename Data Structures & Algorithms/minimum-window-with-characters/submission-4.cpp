class Solution {
public:

    bool isEqual(std::map<char, int> a, std::map<char, int> b) {
        bool isMatched = true;
        for(char c = 'A'; c <= 'Z'; c++) {
            if (a[c] < b[c]) return false;
        }
        for(char c = 'a'; c <= 'z'; c++) {
            if (a[c] < b[c]) return false;
        }
        return true;
    }

    string minWindow(string s, string t) {
        // Idea : make a map of t for its frequency. 
        // Since s and t has upper and smaller chars only. We can use arrays for the frequency
        std::map<char, int> freqT;
        std::map<char, int> freqS;
        int left =0; int right = 0;
        for(char c = 'A'; c <= 'Z'; c++) {
            freqT[c] = 0;
            freqS[c] = 0;
        }
        for(char c = 'a'; c <= 'z'; c++) {
            freqT[c] = 0;
            freqS[c] = 0;
        }
        for (char c: t) {
            freqT[c] ++;
        }
        int minWindow = s.size() + 1;
        int finalL = -1;int finalR = -1;
        for (right= 0; right<s.size(); right ++) {
            freqS[s[right]] ++;
            while (isEqual(freqS, freqT)) {
                if (minWindow >( right-left + 1))
                {
                    minWindow =  right-left + 1;
                    finalL = left;
                    finalR = right+1;
                }
                
                
                freqS[s[left]]--;
                left +=1;
                    
            }
        }
        if (finalL == -1) {
            return "";
        }
        return s.substr( finalL,  minWindow);
    }
};
