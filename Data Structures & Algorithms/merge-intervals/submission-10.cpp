class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<int> num(10001, 0);
        vector<bool> singles(10001, false);

        for (const auto& inter:intervals) {
            if (inter[0]==inter[1]) {
                singles[inter[0]] = true;
                continue;
            }
            num[inter[0]]++;
            num[inter[1]]--;
        }

        vector<vector<int>> res;
        
        int start;
        int count = 0;
        int inInter = false;
        for(int i=0; i<10001; i++) {
            count += num[i];


            if(count > 0 && inInter == false) {
                start = i;
                inInter = true;
            } else if (count == 0 && inInter==true) {
                inInter = false;
                res.push_back({start, i});
            } else if (singles[i]==true && inInter == false) {
                res.push_back({i, i});
            }

        }

        return res;
    }
};