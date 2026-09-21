class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        temp = ''
        if not digits:
            return []
        mp = { 
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }

        def helper(i):
            nonlocal temp
            if i == len(digits):
                ans.append(temp)
                return

            current_digit = digits[i]
            letters = mp[current_digit]
            for k in letters:
                
                temp+=k
                helper(i+1)
                temp = temp[:-1]

        helper(0)
        return ans