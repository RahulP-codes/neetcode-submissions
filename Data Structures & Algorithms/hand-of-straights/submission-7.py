class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for h in hand:
            count[h] = count.get(h, 0) + 1

        hand2 = sorted(list(set(hand)))
        print(hand2)

        h = 0
        while h < len(hand2):
            num = hand2[h]
            if count[num] > 0:
                for i in range(num, num+groupSize, 1):
                    if not i in count or count[i] == 0:
                        return False
                    count[i] -= 1
            else:
                h += 1

        return True