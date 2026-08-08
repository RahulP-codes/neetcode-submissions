class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = [0]*1001
        
        for np, inp, outp in trips:
            points[outp] -= np
            points[inp] += np

        filled = 0
        for p in points:
            filled += p
            if filled > capacity:
                return False

        return True
        