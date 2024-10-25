#include <algorithm>
class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        vector<double>averages;
        while(nums.size()!=0){
            auto min_it = min_element(nums.begin(),nums.end());
            auto max_it = max_element(nums.begin(),nums.end());
            double average = (*min_it + *max_it)/2.0;
            int min_index = distance(nums.begin(),min_it);
            int max_index = distance(nums.begin(),max_it);
            averages.push_back(average);
            if (min_index > max_index) {
                nums.erase(nums.begin() + min_index); 
                nums.erase(nums.begin() + max_index); 
            } else {
                nums.erase(nums.begin() + max_index); 
                nums.erase(nums.begin() + min_index); 
            }
        }
                if (!nums.empty()) {
            averages.push_back(nums[0]);
        }
        auto min_a = min_element(averages.begin(),averages.end());
        return *min_a;
    }
};