class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        ops = {'+': operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv}
        total = 0
        currentNums = list()
        for r in tokens: 
 
            if r in ops:
                
                total = int(ops[r](currentNums[-2], currentNums[-1]))
                currentNums.pop()
                currentNums.pop()
                currentNums.append(total)
                
            else: 
                currentNums.append(int(r))
        return currentNums[-1]