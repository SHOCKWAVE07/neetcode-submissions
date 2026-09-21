class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for i in s:
            if ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('Z') or ord('0')<= ord(i) <= ord('9'):
                if ord('A')<=ord(i)<=ord('Z'):
                    st+= chr(ord(i) - ord('A') + ord('a'))
                else:
                    st+=i


        print(st)

        i, j = 0 , len(st)-1

        while(i<j):

            if st[i] != st[j]:
                return False
            else:
                i+=1
                j-=1

        return True
        