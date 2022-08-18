class Solution:
    def removeLeadingZeros(self, arr):
        ans = ""
        nonZeroValue = False

        for i in range(len(arr)):
            if arr[i] != 0:
                nonZeroValue = True

            if nonZeroValue == True:
                ans += str(arr[i])

        return ans

    def calc_Sub(self, arr,  n, brr, m):
        # Complete the function
        l = max(n, m)
        ans = [0] * (l)
        i, j, k, borrow = n - 1, m - 1, l - 1, 0

        while i >= 0 or j >= 0:
            num = borrow
            if i >= 0:
                num += arr[i]
            if j >= 0:
                num -= brr[j]

            if num < 0:
                num += 10
                borrow = -1
            else:
                borrow = 0

            ans[k] = num

            k -= 1
            if i >= 0:
                i -= 1
            if j >= 0:
                j -= 1

        return self.removeLeadingZeros(ans)
