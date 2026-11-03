class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False
        l, r = 0, len(matrix)-1
        while l <= r:
            m = int(l + (r-l)/2)
            if target == matrix[m][0]:
                return True
            elif target < matrix[m][0]:
                r = m-1
            elif target > matrix[m][-1]:
                l = m+1
            else:
                lc, rc = 0, len(matrix[m])-1
                while lc <= rc:
                    mc = int(lc + (rc-lc)/2)
                    if target == matrix[m][mc]:
                        return True
                    elif target < matrix[m][mc]:
                        rc = mc-1
                    else:
                        lc = mc+1
                break

        return False