class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        if r == 0 and len(matrix[0]) == 1:
            if target == matrix[0][0]:
                return True
            else:
                return False
        while l <= r:
            m = (l+r)//2
            if matrix[m][-1] == target:
                return True
            elif matrix[m][-1] < target:
                l = m+1
            elif matrix[m][-1] > target and matrix[m][0]> target:
                r = m-1
            else:
                lc, rc = 0, len(matrix[m])-1
                while lc <= rc:
                    mc = (lc+rc)//2
                    if matrix[m][mc] == target:
                        return True
                    elif matrix[m][mc] < target:
                        lc = mc+1
                    else:
                        rc = mc-1
                r = m-1
        
        return False