#include <vector>
class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max_value = 0;
        
        for(int i = 0; i < accounts.size(); i++){
            int temp = 0;
            for(int j = 0; j < accounts[i].size(); j++){
                temp+=accounts[i][j];
        }
            max_value = (max_value > temp)?max_value:temp;
        }
        return max_value;
    }
};