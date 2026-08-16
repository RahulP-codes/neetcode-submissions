class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)

        rcount = 0
        for c in senate:
            if c == 'R':
                rcount += 1
        dcount = len(senate) - rcount

        # print(dcount, rcount)
        rvote, dvote = 0, 0
        while rcount and dcount:
            # print(q)
            cur = q.popleft()

            if cur == 'R':
                if dvote:
                    dvote -= 1
                    rcount -= 1
                    continue
                rvote += 1
            else:
                if rvote:
                    dcount -= 1
                    rvote -= 1
                    continue
                dvote += 1

            q.append(cur)

        return "Radiant" if rcount else "Dire"
        