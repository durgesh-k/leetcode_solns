class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        elements=1
        triangle=[[]*i for i in range(numRows)]
        for i in range(numRows):
            for j in range(elements):
                if j==0 or j==elements-1:
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i-1][j-1]+triangle[i-1][j])
            elements+=1
        return triangle