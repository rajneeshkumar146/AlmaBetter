def floodFill_01(sr, sc, er, ec, vis, ans):
    if sr == er and sc == ec:
        print(ans)
        return 1

    vis[sr][sc] = True
    count = 0
    # for right movement
    if sr + 0 <= er and sc + 1 <= ec and vis[sr + 0][sc + 1] == False:
        count += floodFill_01(sr + 0, sc + 1, er, ec, vis, ans + 'r')

    # for left movement
    if sr + 0 <= er and sc - 1 >= 0 and vis[sr + 0][sc - 1] == False:
        count += floodFill_01(sr + 0, sc - 1, er, ec, vis, ans + 'l')

    # for down movement
    if sr + 1 <= er and sc + 0 <= ec and vis[sr + 1][sc + 0] == False:
        count += floodFill_01(sr + 1, sc + 0, er, ec, vis, ans + 'd')

    # for up movement
    if sr - 1 >= 0 and sc + 0 >= 0 and vis[sr - 1][sc + 0] == False:
        count += floodFill_01(sr - 1, sc + 0, er, ec, vis, ans + 'u')

    vis[sr][sc] = False
    return count


def maximumMoves(sr, sc, er, ec, vis):
    if sr == er and sc == ec:
        return 0

    vis[sr][sc] = True
    moves = -1
    # for right movement
    if sr + 0 <= er and sc + 1 <= ec and vis[sr + 0][sc + 1] == False:
        myMove = maximumMoves(sr + 0, sc + 1, er, ec, vis)
        if myMove != -1:
            moves = max(moves, myMove + 1)

    # for left movement
    if sr + 0 <= er and sc - 1 >= 0 and vis[sr + 0][sc - 1] == False:
        myMove = maximumMoves(sr + 0, sc - 1, er, ec, vis)
        if myMove != -1:
            moves = max(moves, myMove + 1)

    # for down movement
    if sr + 1 <= er and sc + 0 <= ec and vis[sr + 1][sc + 0] == False:
        myMove = maximumMoves(sr + 1, sc + 0, er, ec, vis)
        if myMove != -1:
            moves = max(moves, myMove + 1)

    # for up movement
    if sr - 1 >= 0 and sc + 0 >= 0 and vis[sr - 1][sc + 0] == False:
        myMove = maximumMoves(sr - 1, sc + 0, er, ec, vis)
        if myMove != -1:
            moves = max(moves, myMove + 1)

    vis[sr][sc] = False
    return moves


def floodFill():
    sr, sc, er, ec = 0, 0, 2, 2
    vis = []   # never use this statement vis = [[False] * 3] * 3
    for i in range(er + 1):
        v = []
        for j in range(ec + 1):
            v.append(False)
        vis.append(v)

    # print(floodFill_01(sr, sc, er, ec, vis, ""))
    print(maximumMoves(sr, sc, er, ec, vis))


def floodFill_02(sr, sc, er, ec, vis, dir, dirPath, ans):
    if sr == er and sc == ec:
        print(ans)
        return 1

    vis[sr][sc] = True
    count = 0

    for d in range(len(dir)):
        r = sr + dir[d][0]
        c = sc + dir[d][1]

        if r >= 0 and c >= 0 and r <= er and c <= ec and vis[r][c] == False:
            count += floodFill_02(r, c, er, ec, vis, dir,
                                  dirPath, ans + dirPath[d])

    vis[sr][sc] = False
    return count


def floodFill_2():
    sr, sc, er, ec = 0, 0, 2, 2
    vis = []   # never use this statement vis = [[False] * 3] * 3
    for i in range(er + 1):
        v = []
        for j in range(ec + 1):
            v.append(False)
        vis.append(v)

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    dirPath = ['R', 'L', 'D', 'U']

    print(floodFill_02(sr, sc, er, ec, vis, dir, dirPath, ""))


# https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
