class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []

        

    def push(self, val: int) -> None:
        self.arr.append(val)

        val = min(val,self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
        

    def pop(self) -> None:
        self.arr.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

        
