class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        h,w = len(matrix),len(matrix[0])
        # go through first row and first col to see if they need to be zeroed out
        toprowz, leftcolz = False, False
        for i in range(0,h):
            if matrix[i][0]==0:
                leftcolz = True
                break
        for i in range(0,w):
            if matrix[0][i]==0:
                toprowz = True
                break
        
        # go through all i j except first row and first col
        # mark 0,j and i,0 
        for i in range(1, h):
            for j in range(1, w):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # go through first fow and first col except 0,0 and zero out 
        for i in range(1,h):
            if matrix[i][0]==0:
                for j in range(1, w):
                    matrix[i][j] = 0
        for i in range(1,w):
            if matrix[0][i]==0:
                for j in range(1, h):
                    matrix[j][i] = 0
                
        # zero out first row or first col
        if toprowz:
            for i in range(0, w):
                matrix[0][i] = 0
        if leftcolz:
            for i in range(0, h):
                matrix[i][0] = 0
        