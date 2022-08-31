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

    digit = str[0] - '0'
    word = words[digit]
    smallAns = keyPadProblem(str[1:], words)
    


    
    return []


words = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

