class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while True:
            len_nums = len(nums)
            if i >= len_nums:
                break

            if nums[i] == val:
                nums.pop(i)

            else:
                i=i+1