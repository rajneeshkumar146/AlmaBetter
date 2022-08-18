def isPlandrome(str):
    l = len(str)
    i, j = 0, l - 1

    while i < j:
        if str[i] != str[j]:
            return False

        i += 1
        j -= 1

    return True


def printAllPalindromicSubString(str):
    l = len(str)

    for i in range(l):
        for j in range(i, l):
            substr = str[i: j + 1]
            if isPlandrome(substr):
                print(substr)


# aaaabbbcdeffggggg -> a4b3cdef2g5
def compress(str):

    return str

printAllPalindromicSubString("abbaccab")
