class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Bottom up approach
        # time-O(n)
        # space-O(1)
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    # topdown
