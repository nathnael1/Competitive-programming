class Solution {
public:
    int subtractProductAndSum(int n) {
        string s = to_string(n);
        int sum = 0;
        int multiplication = 1;
        for(char word: s){
            sum+= word - '0';
            multiplication*= word - '0';
        }
        return multiplication - sum;
    }
};