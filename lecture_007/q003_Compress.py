# "aaaagggghijkkkllll"  -> "aghijkl"
def removeDuplicatesFromSortedString(str):
    l = len(str)

    if l <= 1:
        return str

    res = str[0]
    i = 1
    while i < l:
        while i < l and str[i] == res[len(res) - 1]:
            i += 1

        if i < l:
            res += str[i]

        i += 1

    return res


def compressString(s):
    l = len(s)

    if l <= 1:
        return s

    res = s[0]
    i = 1
    while i < l:
        count = 1
        while i < l and s[i] == res[len(res) - 1]:
            i += 1
            count += 1

        if count > 1:
            res += str(count)

        if i < l:
            res += s[i]

        i += 1

    return res


# "ababadfa"  -> "abdf"
# T: O(N)
# T: O(NLogN)  if i use sorting
def removeDuplicatesFromString(s):
    freq = {}
    l = len(s)

    for i in range(l):
        ch = s[i]
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    i = ord('a')
    res = ""
    while i <= ord('z'):
        ch = chr(i)
        if ch in freq:
            # print(ch, " -> ", freq[ch])
            res += ch
        i += 1

    return res
