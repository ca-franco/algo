## Find the target in a matrix.
## It is understood that there is search space given
## but a intuitive search space has to be identified.
##
## Time complexity: O(log(m*n))
## Space complexity: O(1)
## 

def find_target_matrix(matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        r = mid // n
        c = mid % n

        if target < matrix[r][c]:
            right = mid - 1
        elif target > matrix[r][c]:
            left = mid + 1
        else: 
            # target and mid is equal
            return True
    return False


