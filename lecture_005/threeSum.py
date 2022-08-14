class Solution:
    def twoSumSolution(self, arr: List[int], tar: int, si: int, ei: int) -> List[int]:
        ans = []
        while si < ei:
            sum_ = arr[si] + arr[ei]
            if sum_ == tar:
                ans.append([arr[si], arr[ei]])
                si += 1
                ei -= 1

                while si < ei and arr[si] == arr[si - 1]:
                    si += 1
                while si < ei and arr[ei] == arr[ei + 1]:
                    ei -= 1

            elif sum_ < tar:
                si += 1
            else:
                ei -= 1

        return ans

    def createAns(self, fixNumber, smallAnsList, res):
        for innerList in smallAnsList:
            innerList.append(fixNumber)
            res.append(innerList)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        si, ei = 0, l - 1
        res = []
        while si < ei:
            newtarget = 0 - nums[si]
            smallAns = self.twoSumSolution(nums, newtarget, si + 1, ei)
            self.createAns(nums[si], smallAns, res)
            si += 1
            while si < ei and nums[si] == nums[si - 1]:
                si += 1

        return res


# HomeWork: https://leetcode.com/problems/4sum/
