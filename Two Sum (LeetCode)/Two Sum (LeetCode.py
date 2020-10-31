class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums_len = len(nums)

        for i in range(nums_len-1):
            for j in range(i+1, nums_len):
                if (nums[i] + nums[j] == target):
                    output.append(i)
                    output.append(j)
                    return output