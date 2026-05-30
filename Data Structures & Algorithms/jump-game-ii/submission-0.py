class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        #Three vars, one for our jump count, one for the distance of covered jumps from our last jump, and one for the distance of the maximum next range of jumps covered
        jumps = 1
        cur_dist = nums[0]
        next_dist = nums[0]

        #One pass, update our distance and next distance accordingly, increasing our amount of jumps whenever a range is surpassed
        for i in range(len(nums) - 1):
            next_dist = max(next_dist, nums[i] + i)
            if i >= cur_dist:
                cur_dist = next_dist
                jumps += 1

        #Return our result
        return jumps
            