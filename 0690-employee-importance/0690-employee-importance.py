"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        print(employees[0].id)
        emp_map = {
            e.id: e for e in employees
        }

        def dfs(emp_id):
            employee = emp_map[emp_id]
            return employee.importance + sum( dfs(i) for i in employee.subordinates ) 

        return dfs(id)


        