class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a,b):
            return a+b
        def sub(a,b):
            return a-b
        def mul(a,b):
            return a*b
        def div(a,b):
            return int(a/b)

        ops = {
                "+": add,
                "-": sub,
                "/": div,
                "*": mul
            }
        
        stack = []
        for i in tokens:
            if i in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[i](a,b))
            else:
                stack.append(int(i))
        
        return stack[0]