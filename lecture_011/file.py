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
def mazePath(sr, sc, er, ec, ans, MyAns):

    return -1
