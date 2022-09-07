def floodFill_01(self, sr, sc, er, ec, vis, ans, myAns):
    if sr == er and sc == ec:
        myAns.append(ans)
        return 1

    vis[sr][sc] = 0  # block that cell
    count = 0
    # for down movement
    if sr + 1 <= er and sc + 0 <= ec and vis[sr + 1][sc + 0] == 1:
        count += self.floodFill_01(sr + 1, sc + 0,
                                   er, ec, vis, ans + 'D', myAns)

    # for left movement
    if sr + 0 <= er and sc - 1 >= 0 and vis[sr + 0][sc - 1] == 1:
        count += self.floodFill_01(sr + 0, sc - 1,
                                   er, ec, vis, ans + 'L', myAns)

    # for right movement
    if sr + 0 <= er and sc + 1 <= ec and vis[sr + 0][sc + 1] == 1:
        count += self.floodFill_01(sr + 0, sc + 1,
                                   er, ec, vis, ans + 'R', myAns)

    # for up movement
    if sr - 1 >= 0 and sc + 0 >= 0 and vis[sr - 1][sc + 0] == 1:
        count += self.floodFill_01(sr - 1, sc + 0,
                                   er, ec, vis, ans + 'U', myAns)

    vis[sr][sc] = 1  # free that cell
    return count


def findPath(self, mat, n):
    sr, sc, er, ec = 0, 0, n - 1, n - 1
    myAns = []
    self.floodFill_01(sr, sc, er, ec, mat, "", myAns)
    myAns.sort()

    return myAns
