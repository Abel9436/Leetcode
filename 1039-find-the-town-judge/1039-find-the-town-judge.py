class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        in_degree = [0] * n
        out_degree = [0] * n

        for p , t in trust:
            in_degree[p -1] +=1
            out_degree[t -1] +=1
        print(in_degree , out_degree)

        for i in range(n):
            if in_degree[i] == 0 and out_degree[i] == n - 1:
                return i + 1

        # graph = defaultdict(list)


        # for p , t in trust:
        #     graph[p].append(t)

        # keys = graph.keys()

        # for i in range(1, n + 1):
        #     if i not in keys:
        #         return i
        return -1
        # print(graph)        