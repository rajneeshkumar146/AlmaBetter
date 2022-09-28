def subsequence(str):
    if len(str) == 0:
        return [""]

    ch = str[0]
    smallList = subsequence(str[1:])
    myAns = []
    for s in smallList:
        myAns.append(s)
        myAns.append(ch + s)

    return myAns


def keyPadProblem(str, words):
    if len(str) == 0:
        return [""]

    digit = ord(str[0]) - ord('0')
    word = words[digit]
    smallAns = keyPadProblem(str[1:], words)

    myAns = []
    for i in range(len(word)):
        ch = word[i]
        for s in smallAns:
            myAns.append(ch + s)

    return myAns


words = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

# sp: starting point, ep: ending point


def boardPath(sp, ep):
    if sp == ep:
        return [""]

    myAns = []
    dice = 1
    while dice <= 6 and sp + dice <= ep:
        smallAns = boardPath(sp + dice, ep)
        for s in smallAns:
            myAns.append(str(dice) + s)
        dice += 1

    return myAns


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
    allPermutation("abc",vis,0, myAns,"")
    print(myAns)


# no extra space
def allUniquePermutation(str, vis, count, myAns, ans):
    return 1

def allUniquePermutation():
    myAns = []
    vis = [False] * 3
    allUniquePermutation("aba",vis,0, myAns,"")
    print(myAns)