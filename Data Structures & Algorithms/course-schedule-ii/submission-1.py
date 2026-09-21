class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        mp = {i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            mp[i].append(j)

        visited = set()
        cycle = set()
        ans = []
        def dfs(key):
            if key in cycle:
                return False

            if key in visited:
                return True

            cycle.add(key)

            for val in mp[key]:
                if not dfs(val):
                    return False

            cycle.remove(key)
            visited.add(key)
            ans.append(key)

            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans