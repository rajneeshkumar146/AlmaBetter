def allPermutation(str, vis, count, myAns, ans):
    if count == len(str):
        myAns.append(ans)
        return

    l = len(str)
    for i in range(l):
        if vis[i] == False:
            vis[i] = True
            allPermutation(str, vis, count + 1, myAns, ans + str[i])
            vis[i] = False


def allPermutation():
    myAns = []
    vis = [False] * 3
    allPermutation("abc", vis, 0, myAns, "")
    print(myAns)


# no extra space
def allUniquePermutations(str, vis, count, myAns, ans):
    if count == len(str):
        myAns.append(ans)
        return

    prevChar = '$'
    for i in range(len(str)):
        if vis[i] == False and prevChar != str[i]:
            vis[i] = True
            allUniquePermutations(str, vis, count + 1, myAns, ans + str[i])
            vis[i] = False
            prevChar = str[i]


def allUniquePermutation():
    str = "aaaaaaa"

    str = ''.join(sorted(str))   # NLog(N)
    vis = [False] * len(str)
    myAns = []

    allUniquePermutations(str, vis, 0, myAns, "")
    print(myAns)


allUniquePermutation()

# Leetcode 46 and 47 for you.


# T: O(N), S: O(N), Constraints: str contains only alphabetical Characters
def generateStringOnFreq(ch, freq):
    return ""


def sortString(str):
    ans = ""
    return ans

# sr: starting Row, sc: starting Column, er: ending Row, ec: Ending Column,


def mazePath(sr, sc, er, ec, ans):
    if sr == er and sc == ec:
        print(ans)
        return 1

    count = 0
    if sr + 1 <= er:  # Horizontal
        count += mazePath(sr + 1, sc, er, ec, ans + "H")

    if sr + 1 <= er and sc + 1 <= ec:  # Diagonal
        count += mazePath(sr + 1, sc + 1, er, ec, ans + "D")

    if sc + 1 <= ec:  # Vertical
        count += mazePath(sr, sc + 1, er, ec, ans + "V")

    return count

def mazePathJump(sr, sc, er, ec, ans):
    if sr == er and sc == ec:
        print(ans)
        return 1

    count = 0

    jump = 1
    while sr + jump <= er:  # Horizontal
        count += mazePathJump(sr + jump, sc, er, ec, ans + "H" + str(jump))
        jump += 1

    jump = 1
    while sr + jump <= er and sc + jump <= ec:  # Diagonal
        count += mazePathJump(sr + jump, sc + jump, er, ec, ans + "D" + str(jump))
        jump += 1

    jump = 1
    while sc + jump <= ec:  # Vertical
        count += mazePathJump(sr, sc + jump, er, ec, ans + "V" + str(jump))
        jump += 1

    return count


print(mazePathJump(0, 0, 2, 2, ""))
