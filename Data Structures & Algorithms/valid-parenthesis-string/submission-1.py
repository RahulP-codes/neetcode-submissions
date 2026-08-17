class Solution:
    def checkValidString(self, s: str) -> bool:
        openc = 0
        free = 0
        for c in s:
            if c == "(":
                openc += 1
            elif c == "*":
                free += 1
            else:
                if openc > 0:
                    openc -= 1
                else:
                    if free > 0:
                        free -= 1
                    else:
                        return False

        openc = 0
        free = 0
        print('hi')
        for c in s[::-1]:
            if c == ")":
                openc += 1
            elif c == "*":
                free += 1
            else:
                if openc > 0:
                    openc -= 1
                else:
                    if free > 0:
                        free -= 1
                    else:
                        return False
        
        # while openc > 0:
        #     free -= 1
        #     if free < 0:
        #         return False
        #     openc -= 1

        return True