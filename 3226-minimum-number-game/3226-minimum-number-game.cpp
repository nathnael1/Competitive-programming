#include <algorithm>
class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        vector<int> res;
        while(nums.size() > 1){
            auto minElement = min_element(nums.begin(),nums.end());
            int element1 = *minElement;
            nums.erase(minElement);
            if(nums.empty()){
                res.push_back(*minElement);
                break;
            }
            auto minElement1 = min_element(nums.begin(),nums.end());
            int element2 = *minElement1;
            nums.erase(minElement1);
            res.push_back(element2);
            res.push_back(element1);
        
        }
        return res;
    }
};