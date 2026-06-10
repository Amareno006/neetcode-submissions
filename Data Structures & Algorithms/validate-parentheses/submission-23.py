class Solution:
    def isValid(self, s: str) -> bool:


        pairs = {'(' : ')', '[': ']', '{' : '}'}
        stack = []
        for r in s: 
            if r in pairs:
                stack.append(r)

            if r not in pairs:
                if len(stack) == 0: 
                    return False
                elif r == pairs[stack[-1]]:
                    stack.pop()
                
                else: 
                    return False



        return len(stack) == 0