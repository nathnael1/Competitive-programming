#include <vector>
#include <numeric>
using namespace std;
class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int>numbers;
        for(int i = 0; i < operations.size(); i++)
        {
            if(operations[i] == "D"){
                numbers.push_back(numbers.back() * 2);
            }else if(operations[i] == "C"){
                numbers.pop_back();
            }else if(operations[i] == "+"){
                numbers.push_back(numbers.back() + numbers[numbers.size()-2]);
            }else{
                numbers.push_back(stoi(operations[i]));
            }
        }
        return accumulate(numbers.begin(),numbers.end(),0);
    }
};