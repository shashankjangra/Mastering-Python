class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        value = False
        for i in range(len(arr)):
            for j in range(len(arr)):
                check_i_multiply = arr[i] * 2
                check_i_add = arr[i] + arr[i]
                if check_i_multiply == arr[j] and check_i_add == arr[j] and i!=j:
                    value = True

        return value