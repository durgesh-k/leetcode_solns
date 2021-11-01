class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target>=matrix[i][0] and target<=matrix[i][-1]:
                for j in matrix[i]:
                    if target==j:
                        return True
        return False