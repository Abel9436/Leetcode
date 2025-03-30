class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last_occurence={ 
            val: index for index , val in enumerate(s)
        }

        print(last_occurence)

        left,right=0,0
        ans=[]
        
        for index , value in enumerate(s):
            right=max(right,last_occurence[value])

            if index == right:

                ans.append(right-left+1)
                left=right+1
        return (ans)
