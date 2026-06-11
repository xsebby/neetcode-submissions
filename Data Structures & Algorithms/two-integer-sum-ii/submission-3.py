class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)
        ans = []
        while l <= r:
            if (numbers[l] + numbers[r-1] > target):
                r = r -1
            elif (numbers[l] + numbers[r-1] < target):
                l = l +1
            else:
                ans.append(l+1)
                ans.append(r)
                return ans