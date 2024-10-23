class Solution {
public:
    int numberOfMatches(int n) {
        int matches = 0;
        int teams = n;
        while(teams > 1){
            if(teams %2 == 0){
                matches+= teams/2;
                teams = teams/2;
            }else{
                matches+= teams/2;
                teams = (teams/2) + 1;
            }
        }
        return matches;
    }
};