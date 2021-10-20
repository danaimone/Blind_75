class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        rows, cols, = set(), set()
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        for i in range(row):
            for j in range(col):
                if i in rows or j in cols:
                    matrix[i][j] = 0
                
            
        