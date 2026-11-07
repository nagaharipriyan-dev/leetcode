class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)

        for ind in range(nums_len-1):

            curr_num = nums[ind]

            elem_to_find = target - curr_num

            for j_ind in range(ind+1, nums_len):

                if nums[j_ind] == elem_to_find:
                    return [ind, j_ind]
