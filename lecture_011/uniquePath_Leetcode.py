class Solution:
    def UniquePath(self,sr, sc, er, ec,obstacleGrid):
        if sr == er and sc == ec:
            return 1

        count = 0
        if sr + 1 <= er and obstacleGrid[sr + 1][sc]  == 0:  # Horizontal
            count += self.UniquePath(sr + 1, sc, er, ec,obstacleGrid)

        if sc + 1 <= ec and obstacleGrid[sr][sc + 1]  == 0:  # Vertical
            count += self.UniquePath(sr, sc + 1, er, ec,obstacleGrid)

        return count


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        er = len(obstacleGrid) - 1
        ec = len(obstacleGrid[0]) - 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[er][ec] == 1:
            return 0
        
        return self.UniquePath(0,0,er,ec,obstacleGrid)