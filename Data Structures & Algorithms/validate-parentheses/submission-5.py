class Solution:
    def isValid(self, s: str) -> bool:

        a = []

        for i in s:
            if i in ['(','[','{']:
                a.append(i) 
            else:
                if not a:
                    return False

                if i == ')':
                    if a[-1]=='(':
                        a.pop()
                    else:
                        return False
                
                elif i == ']':
              
                    if a[-1]=='[':
                        a.pop()
                    else:
                        return False

                elif i == '}':
                    if a[-1] == '{':
                        a.pop()
                    else:
                        return False

        if not a:
            return True
        else: 
            return False
                

        