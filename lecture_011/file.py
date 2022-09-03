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
    str = "aabaabb"
    
    str = ''.join(sorted(str))
    vis = [False] * len(str)
    myAns = []

    allUniquePermutation(str,vis,0, myAns,"")
    print(myAns)

# T: O(N), S: O(N)
def sortString(str):
    ans = ""

    return ans
