#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class TimeMap {
public:
    unordered_map<string, vector<pair<string, int>>> myMap;

    TimeMap() {}

    void set(string key, string value, int timestamp) {
        myMap[key].push_back({value, timestamp});
    }

    string get(string key, int timestamp) {
        auto it = myMap.find(key);

        if (it == myMap.end()) {
            return "";
        }

        auto& v = it->second;

        int left = 0;
        int right = v.size() - 1;
        string result = "";

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (v[mid].second <= timestamp) {
                // Valid candidate. Look for a later timestamp.
                result = v[mid].first;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }
};