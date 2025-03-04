class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x: abs(x[0]-x[1]), reverse = True)

        a_count =  0
        b_count = 0
        ans = 0
        for cost_a,cost_b in costs:

            if cost_a < cost_b :
                if a_count  < len(costs)//2:
                    a_count +=1
                    ans+= cost_a
                else:
                    b_count +=1
                    ans +=cost_b
            else:
                if b_count < len(costs)//2:
                    b_count +=1
                    ans+= cost_b
                else:
                    a_count +=1
                    ans += cost_a
        return ans

        