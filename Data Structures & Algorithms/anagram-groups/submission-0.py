class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        visited = [False] * n
        output = []

        for i in range(n):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, n):
                if not visited[j]:
                    if sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])
                        visited[j] = True

            output.append(group)   # <-- This should be inside the outer loop

        return output