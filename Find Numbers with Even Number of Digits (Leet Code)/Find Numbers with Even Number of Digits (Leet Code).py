class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        for i in nums:
            even =0
        for i in nums:
            a = str(i)
            b=len(a)

            if b%2 == 0:
                even = even +1

        return even