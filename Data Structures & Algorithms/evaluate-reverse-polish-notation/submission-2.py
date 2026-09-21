class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for i in tokens:

            if i not in ['+','-','*','/']:
                print(int(i))
                stack.append(int(i))
            else:
                if len(stack) > 1:
                    num2 = stack.pop()
                    num1 = stack.pop()

                    if i == '+':
                        temp = num1 + num2
                    elif i == '-':
                        temp = num1-num2
                    elif i == '*':
                        temp = num1*num2
                    else:
                        temp = int(num1/num2)
                    print(temp)
                    stack.append(temp)

                else:
                    break

        return stack[-1]
        