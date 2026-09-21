class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''

        for i in strs:
            for j in i:
                string+=j
            string+=';:'

        return string

    def decode(self, s: str) -> List[str]:
        ans = []
        temp=''
        flag = False
        for i in s:
            if i==';':
                flag = True
            elif i==':' and flag:
                ans.append(temp)
                temp=''
                flag=False
            else:
                temp+=i
        return ans
