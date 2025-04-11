class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        #nlkaskz

        graph = defaultdict(list)


        for i, m in enumerate(manager):

            if m != -1:
                graph[m].append(i)
        _max_time = 0

        def dfs(emp_id , curr_time):
            nonlocal _max_time

            _max_time = max(_max_time , curr_time)

            for sub in graph[emp_id]:
                dfs( sub , curr_time + informTime[emp_id])
        
        dfs(headID , 0)

        return _max_time



        print(graph)

            
