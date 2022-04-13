class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        left, right = 0, n-1
        top,down = 0, n-1
        
        val = 1
        while top <= down and left <= right:
            for i in range(left, right+1):
                res[top][i] = val
                val += 1
            
            for i in range(top+1, down+1):
                res[i][right] = val
                val += 1
            
            for i in reversed(range(left, right)):
                if top == down:
                    break
                res[down][i] = val
                val += 1
            for i in reversed(range(top + 1, down)):
                if left == right:
                    break
                res[i][left] = val
                val += 1
            top += 1
            down -= 1
            left += 1
            right -= 1
        return res
