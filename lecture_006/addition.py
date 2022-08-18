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

    def calc_Sum(self, arr,  n, brr, m):
        # Complete the function
        l = max(n, m) + 1
        ans = [0] * (l)
        i, j, k, carry = n - 1, m - 1, l - 1, 0

        while i >= 0 or j >= 0 or carry != 0:
            num = carry
            if i >= 0:
                num += arr[i]
            if j >= 0:
                num += brr[j]

            digit = num % 10
            carry = num // 10

            ans[k] = digit

            k -= 1
            if i >= 0:
                i -= 1
            if j >= 0:
                j -= 1

        return self.removeLeadingZeros(ans)
