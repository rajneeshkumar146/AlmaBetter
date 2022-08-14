def twoSum(numbers: List[int], target: int):
    l = len(numbers)
    for i in range(l):
        b = target - numbers[i]
        for j in range(i + 1, l):
            if b == numbers[j]:
                return [i + 1, j + 1]

    return []


def twoSum_02(numbers: List[int], target: int) -> List[int]:
    dictionary = {}
    l = len(numbers)
    for i in range(l):
        b = target - numbers[i]
        if b in dictionary:
            return [dictionary[b] + 1, i + 1]

        dictionary[numbers[i]] = i
    return []


def twoSum_03(numbers: List[int], target: int) -> List[int]:
    l, si, ei = len(numbers), 0, len(numbers) - 1
    while si < ei:
        sum = numbers[si] + numbers[ei]
        if sum == target:
            return [si + 1, ei + 1]
        elif sum < target:
            si += 1
        else:
            ei -= 1

    return []


def twoSum(arr, tar, si, ei):
    ans = []
    while si < ei:
        sum = arr[si] + arr[ei]

        if sum == tar:
            ans.append([si, ei])
            si += 1
            ei -= 1

            while si < ei and arr[si] == arr[si - 1]:
                si += 1
            while si < ei and arr[ei] == arr[ei + 1]:
                ei -= 1

        elif sum < tar:
            si += 1
        else:
            ei -= 1
    
    return ans
