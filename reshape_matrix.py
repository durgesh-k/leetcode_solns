class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        oned=[]
        index=0
        for i in mat:
            for j in mat[index]:
                oned.append(j)
            index+=1
        result=[[0 for i in range(c)] for j in range(r)]
        index=0
        if c*r==len(oned):
            for i in range(r):
                for j in range(c):
                    result[i][j]=oned[index]
                    index+=1
            return result
        else:
            return mat