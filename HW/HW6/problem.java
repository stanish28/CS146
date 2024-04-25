package HW.HW6;

import java.util.*;

public class problem {


public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);  // Sort the array to use two pointers effectively
    List<List<Integer>> res = new ArrayList<>();
    for (int i = 0; i < nums.length - 2; i++) {
        if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {  // Skip duplicates
            int lo = i + 1, hi = nums.length - 1, sum = 0 - nums[i];
            while (lo < hi) {
                if (nums[lo] + nums[hi] == sum) {
                    res.add(Arrays.asList(nums[i], nums[lo], nums[hi]));
                    while (lo < hi && nums[lo] == nums[lo + 1]) lo++;  // Skip duplicates
                    while (lo < hi && nums[hi] == nums[hi - 1]) hi--;  // Skip duplicates
                    lo++; hi--;
                } else if (nums[lo] + nums[hi] < sum) {
                    lo++;
                } else {
                    hi--;
                }
            }
        }
    }
    return res;
}
    
}


