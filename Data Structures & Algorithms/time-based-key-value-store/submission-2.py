class TimeMap:

    def __init__(self):
        self.arr = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
            self.arr[key] = []
        
        self.arr[key].append([value,timestamp])
       

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.arr.get(key,[])

        s , e = 0 , len(values)-1

        while s<=e:
            mid = s + (e-s)//2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                s = mid+1

            else:
                e = mid-1

        return res
            


            

        
