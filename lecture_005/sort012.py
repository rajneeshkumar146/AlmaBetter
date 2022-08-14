class Solution:
    def sortColors(self, arr: List[int]) -> None:
        itr = 0
        pt = -1
        n = len(arr)
        pt2 = n - 1 

        while itr <= pt2:
            if arr[itr] == 0:
                pt += 1
                arr[pt], arr[itr] = arr[itr], arr[pt]
                itr += 1
            elif arr[itr] == 1:
                itr += 1
            else:
                arr[pt2], arr[itr] = arr[itr], arr[pt2]
                pt2 -= 1
