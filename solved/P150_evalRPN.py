__author__ = 'Connor'

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for tk in tokens:
            if tk == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 + op1))
            elif tk == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 - op1))
            elif tk == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 * op1))
            elif tk == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2 * 1.0 / op1))
            else:
                stack.append(int(tk))
        return stack[0]

if __name__ == '__main__':
    so =Solution()
    aa = ["2", "1", "+", "3", "*"]
    aa = ["4", "13", "5", "/", "+"]
    aa = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ans = so.evalRPN(aa)
    print(ans)