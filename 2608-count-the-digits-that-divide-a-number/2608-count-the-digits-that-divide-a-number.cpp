#include <string>
class Solution {
public:
    int countDigits(int num) {
        int counter = 0;
        string nums = to_string(num);
        for(char d: nums){
            int digit = d - '0';
            if(num%digit == 0){
                counter++;
            }
        }
        return counter;
    }
};