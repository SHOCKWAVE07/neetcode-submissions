class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            num = temperatures[i]
            while stack and stack[-1][0]<num:
                out = stack.pop()
                res[out[1]] = i - out[1]
                
            stack.append((num,i))

        return res


        