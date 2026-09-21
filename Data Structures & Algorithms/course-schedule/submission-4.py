class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mp = { i : [] for i in range(numCourses)}

        for i,j in prerequisites:
                mp[i].append(j)
            

        visited = set()

        def dfs(key):
            if key in visited:
                return False
            
            if mp[key] == []:
                return True
            
            visited.add(key)
            for val in mp[key]:
                if not dfs(val):
                    return False
            visited.remove(key)
            mp[key] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

