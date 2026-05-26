class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        cur_sub_g, cur_sub_l, max_sub = 1, 1, 1

        #Simple, just keep running subarrays based on > or < start, and track the max
        #Handle <, >, and = cases while paying attention to index parity
        for i in range(1, len(arr)):
            if i % 2 == 1:
                if arr[i - 1] > arr[i]:
                    cur_sub_g += 1
                    max_sub = max(max_sub, cur_sub_l)
                    cur_sub_l = 1
                elif arr[i - 1] < arr[i]:
                    cur_sub_l += 1
                    max_sub = max(max_sub, cur_sub_g)
                    cur_sub_g = 1
                else:
                    max_sub = max(max_sub, cur_sub_l, cur_sub_g)
                    cur_sub_l = 1
                    cur_sub_g = 1
            else:
                if arr[i - 1] > arr[i]:
                    cur_sub_l += 1
                    max_sub = max(max_sub, cur_sub_g)
                    cur_sub_g = 1
                elif arr[i - 1] < arr[i]:
                    cur_sub_g += 1
                    max_sub = max(max_sub, cur_sub_l)
                    cur_sub_l = 1
                else:
                    max_sub = max(max_sub, cur_sub_l, cur_sub_g)
                    cur_sub_l = 1
                    cur_sub_g = 1

        return max(cur_sub_l, cur_sub_g, max_sub)
                    

