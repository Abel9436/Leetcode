class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        a_list = defaultdict(list)

        for u ,v in dislikes:
            a_list[u].append(v)
            a_list[v].append(u)
        print(a_list)
        colors = {}
        for node in a_list:
            if node not in colors:
                queue = deque([(node , 0)])
                colors[node] = 0
            
            while queue:

                u , red_color = queue.popleft()

                for v in a_list.get(u , []):

                    if v not in colors:
                        queue.append((v , 1 - red_color))
                        colors[v] = 1 - red_color

                    elif colors[v] == red_color:
                        return False
        return True
