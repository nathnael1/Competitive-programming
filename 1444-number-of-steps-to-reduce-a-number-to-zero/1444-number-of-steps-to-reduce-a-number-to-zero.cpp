class Solution {
public:
    int numberOfSteps(int num) {
        int counter = 0;
        while(num!=0){
            num = (num%2 == 0) ? num/2 : --num;
            counter++;
        }
        return counter;
    }
};