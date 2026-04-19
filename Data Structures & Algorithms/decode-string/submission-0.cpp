class Solution {
public:

    string decodeString(string s) {
        string final = "";
        std::stack <std::pair<int, std::string>> st;
        int i = 0;
        st.push({1, final});
        while (i < s.size()) {
            if (s[i] >= 'a' and s[i] <= 'z') {
                st.top().second = st.top().second + s[i];
            }

            else if ( s[i] == ']') {
                string form = st.top().second;
                int count = st.top().first;
                string finalform = "";
                for (int k = 0; k < count; k++) finalform = finalform + form;
                st.pop();
                st.top().second = st.top().second + finalform;
            } else {
                int j = i;
                while(s[j]!= '[') {
                    j++;
                }
                std:string substrg = s.substr(i, j-i);
                int num = std::stoi(substrg);
                st.push ({num, ""});
                i = j;
            }
            i++;
        }

        // ]

        // [


        // number

        // character 
        return st.top().second;

    }
};