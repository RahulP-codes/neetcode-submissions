class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        one = two = three = False
        for t in triplets:
            if not one:
                if t[0] == target[0] and t[1]<= target[1] and t[2]<= target[2]:
                    one = True
            if not two:
                if t[1] == target[1] and t[0]<= target[0] and t[2]<= target[2]:
                    two = True
            if not three:
                if t[2] == target[2] and t[0]<= target[0] and t[1]<= target[1]:
                    three = True

        return one and two and three