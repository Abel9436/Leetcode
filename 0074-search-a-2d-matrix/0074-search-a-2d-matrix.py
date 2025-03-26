class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mn,mx=0,len(matrix)-1
        best=mx
        while(mx>=mn):
            mid=mn+(mx-mn)//2
            if(matrix[mid][0]==target):
                return True
            elif(matrix[mid][0]<target):
                best=mid
                mn=mid+1
            else:
                mx=mid-1

        print(best)
        mn,mx=0,len(matrix[0])-1
        while(mx>=mn):
            mid=mn+(mx-mn)//2
            if(matrix[best][mid]==target):
                return True
            elif(matrix[best][mid]<target):
                mn=mid+1
            else:
                mx=mid-1
        return False