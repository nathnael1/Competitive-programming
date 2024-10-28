#include <algorithm>
class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        for(int i = 0; i < names.size() - 1; i++){
            for(int j = 0; j < names.size() - 1 -i;j++){
                if(heights[j+1] > heights[j]){

                    swap(heights[j+1], heights[j]);
                    swap(names[j+1], names[j]);
                }
            }
        }
        return names;
    }
};