# coding: utf-8
import time

def quick_sort_1_1(nums):
    def recursive(nums, start, end):
        if start >= end: return
        # choose a index of pivot
        choose_p_idx = end
        nums[end], nums[choose_p_idx] = nums[end], nums[choose_p_idx]
        final_p_idx = start
        for i in xrange(start, end):
            if nums[i] < nums[end]:
                nums[i], nums[final_p_idx] = nums[final_p_idx], nums[i]
                final_p_idx += 1
        nums[end], nums[final_p_idx] = nums[final_p_idx], nums[end]
        
        recursive(nums, start, final_p_idx - 1)
        recursive(nums, final_p_idx + 1, end)
    
    recursive(nums, 0, len(nums) - 1)
    return nums

def quick_sort_1_2(nums):
    def recursive(nums, start, end):
        if start >= end: return
        # choose a index of pivot
        p_start_idx = int(start + end) / 2
        nums[start], nums[p_start_idx] = nums[p_start_idx], nums[start]
        final_p_idx = start + 1
        for i in xrange(start + 1, end + 1):
            if nums[i] >= nums[start]: continue
            nums[i], nums[final_p_idx] = nums[final_p_idx], nums[i]
            final_p_idx += 1
        final_p_idx = final_p_idx - 1
        nums[start], nums[final_p_idx] = nums[final_p_idx], nums[start]
        recursive(nums, start, final_p_idx - 1)
        recursive(nums, final_p_idx + 1, end)
    
    recursive(nums, 0, len(nums) - 1)
    return nums

def quick_sort_2(nums):
    def recursive(nums, start, end):
        if start >= end: return

        pivot_val = nums[start]
        head, tail = start, end
        while head < tail:
            # the loop here is waiting for only one case
            while head < tail:
                if pivot_val > nums[tail]:
                    nums[head] = nums[tail]
                    break
                tail -= 1
            # the loop here is waiting for only one case
            while head < tail:
                if pivot_val < nums[head]:
                    nums[tail] = nums[head]
                    break
                head += 1

        nums[head] = pivot_val
        recursive(nums, start, head - 1)
        recursive(nums, head + 1, end)
    
    recursive(nums, 0, len(nums) - 1)
    return nums
    
def popup_sort(nums):
    for i in xrange(len(nums)):
        for j in xrange(i, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

def print_ret(nums, func):
    nums = [x for x in nums]

    timestp = time.time()
    new_nums = func(nums)
    time_cost = time.time() - timestp
    print 'func:%s time_cost:%.4fs ret:\n%s' %(str(func), time_cost, new_nums)

if __name__ == '__main__':
    nums = [2, 7, 9,10, -1, -8, 5, 10, 1, -3, 4, -6]
    
    print_ret(nums, popup_sort)
    print_ret(nums, quick_sort_1_1)
    print_ret(nums, quick_sort_1_2)
    print_ret(nums, quick_sort_2)