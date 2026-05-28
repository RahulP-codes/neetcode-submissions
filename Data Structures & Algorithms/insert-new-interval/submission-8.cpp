class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        if (intervals.size() == 0) {
            return {newInterval};
        }

        vector<vector<int>> res;

        int start = newInterval[0];
        int end = newInterval[1];

        int prevEnd = -1;
        int insStart = -1;
        bool started = false;
        for(const auto& inter:intervals) {
            int curStart = inter[0];
            int curEnd = inter[1];

            if (prevEnd < start && curStart > start) {
                insStart = start;
                started = true;
            } else if (curStart <= start && start <= curEnd) {
                insStart = curStart;
                started = true;
            }

            if (insStart != -1) {
                if (prevEnd < end && curStart > end) {
                    res.push_back({insStart, end});
                    insStart = -1;
                } else if (curStart <= end && end <= curEnd) {
                    res.push_back({insStart, curEnd});
                    insStart = -1;
                    continue;
                }
            }
            
            if (insStart == -1) {
                res.push_back(inter);
            }
            prevEnd = curEnd;
        }

        if (insStart != -1) {
            res.push_back({insStart, end});
        } 
        if (started == false) {
            res.push_back(newInterval);
        }

        return res;
    }
};
