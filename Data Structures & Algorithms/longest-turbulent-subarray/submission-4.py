class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        curTurb = 1
        maxTurb = 1

        state = True

        for i in range(n-1):
            if curTurb != 1:
                if state and arr[i] > arr[i+1]:
                    state = not state
                    curTurb += 1
                elif not state and arr[i] < arr[i+1]:
                    state = not state
                    curTurb += 1
                else:
                    curTurb = 1

            if arr[i] == arr[i+1]:
                curTurb = 1
            elif curTurb == 1:
                curTurb = 1
                if arr[i] < arr[i+1]:
                    state = True
                else:
                    state = False
                curTurb += 1

            maxTurb = max(maxTurb, curTurb)
            print(i, curTurb, maxTurb)
            i += 1

        return maxTurb