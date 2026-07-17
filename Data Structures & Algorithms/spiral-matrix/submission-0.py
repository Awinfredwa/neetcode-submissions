class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nextdir = {(0,1):(1,0), (1,0):(0,-1), (0,-1):(-1,0), (-1,0):(0,1)}
        d = (0,1)
        i,j=0,0
        h, w = len(matrix), len(matrix[0])
        def inBound(i:int, j:int) -> bool:
            if i<0 or j<0 or i>=h or j>=w:
                return False
            return True 
        res = []
        while True:
            res.append(matrix[i][j])
            # find nexti, nextj
            nexti, nextj = i + d[0], j+d[1]
            if not inBound(nexti, nextj) or matrix[nexti][nextj]==None:
                d = nextdir[d]
                nexti, nextj = i + d[0], j+d[1]
            # reaching the end
            if not inBound(nexti, nextj) or matrix[nexti][nextj]==None:
                break; 
            # mark visited and proceed
            matrix[i][j] = None
            i, j  = nexti, nextj
        return res

        