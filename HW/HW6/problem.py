from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()  # Sort the array to facilitate the two-pointer approach
    res = []
    for i in range(len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):  # Skip duplicates
            lo, hi = i + 1, len(nums) - 1
            sum = -nums[i]
            while lo < hi:
                if nums[lo] + nums[hi] == sum:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1  # Skip duplicates
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1  # Skip duplicates
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < sum:
                    lo += 1
                else:
                    hi -= 1
    return res
