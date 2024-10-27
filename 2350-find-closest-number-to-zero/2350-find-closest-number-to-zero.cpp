class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int max_value[2];
        int value = numeric_limits<int>::max();
        int res = 0;
       for(int i: nums){
            int temp = (i - 0 > 0) ? i : -i;
            if(temp < value){
                value = (i - 0 > 0) ? i : -i;
                res = i;
            }
            if(temp == value){
                res = (i > res) ? i : res;
            }

       } 
       return res;
    }
};