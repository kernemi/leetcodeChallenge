class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ans = defaultdict(int)

        for i in range(len(logs)):
            
            start = logs[i][0]
            end = logs[i][1] - 1
            
            while start <= end:

                ans[start] += 1
                start += 1

        res = sorted(ans.items(), key=lambda x: (-x[1], x[0]))
        return res[0][0]
                


