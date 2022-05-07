#include <vector>
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(),strs.end());
        string string_first = strs[0];
        string string_last = strs.back();
        int count = 0;
        for (int i =0; i < string_first.size(); i++){
            if (string_first[i] == string_last[i]){
                count++;
            }
            else{
                break;
            }
        }
        if (count == 0){
            return "";
        }
        else{
            return string_first.substr(0, count);
        }
    }
};