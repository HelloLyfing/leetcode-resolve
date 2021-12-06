class Solution:
    '''link: https://oj.leetcode.com/problems/3sum-closest/ '''
    def threeSumClosest(self, nums, target):
        nums_len = len(nums)
        if nums_len <= 3:
            return sum(nums)

        self.nums = sorted(nums)
        min_val = float('+inf')
        min_comb = (0, 1, 2)
        for i in xrange(nums_len - 3 + 1):
            #print '1st:%s' %i 
            _2cloest = self._2cloest(i + 1, target - self.nums[i])
            tmp_val = abs(target - self.get_sum(_2cloest + (i,)))

            #print 'new comb: %s' %str(_2cloest + (i,))

            if tmp_val < min_val:
                min_val = tmp_val
                min_comb = _2cloest + (i,)
                #print 'new min: %s' %str(_2cloest + (i,))

        return self.get_sum(min_comb)

    def _2cloest(self, start, target):
        start_pt = start
        end_pt = len(self.nums) - 1
        
        min_val = float('+inf')
        pos = (start_pt, end_pt)
        while start_pt < end_pt:
            #print '2nd:%s 3rd:%s' %(start_pt, end_pt)

            tmp = self.get_sum((start_pt, end_pt,))
            if tmp < target:
                if abs(target - tmp) < min_val:
                    min_val = abs(target - tmp)
                    pos = (start_pt, end_pt)
                start_pt += 1
                continue
            elif tmp > target:
                if abs(target - tmp) < min_val:
                    min_val = abs(target - tmp)
                    pos = (start_pt, end_pt)
                end_pt -= 1
                continue
            elif tmp == target:
                return (start_pt, end_pt,)

        return pos

    def get_sum(self, pos_tuple):
        sum_ = 0
        for pos in pos_tuple:
            sum_ += self.nums[pos]
        return sum_

    
if __name__ == '__main__':
    n_1 = [-1, 2, 1, 4]
    t_1 = 1

    # need 3
    n_2 = [1,1,1,0]
    t_2 = 100

    # need 0
    n_4 = [0, 2, 1, -3]
    t_4 = 1

    n_5 = [-26,84,-85,2,99,42,-28,16,-97,-59,64,-67,-30,18,-15,-11,-60,-79,41,-29,49,-33,21,-8,-73,6,-31,31,-23,82,-34,12,86,38,-4,99,4,63,-13,-42,-4,89,88,-30,0,15,37,-95,-85,15,66,8,43,95,-76,75,-16,48,15,-82,56,83,91,81,-76,-29,7,-77,-42,39,-73,29,43,-60,21,-5,-3,1,32,34,-77,49,68,-1,-63,93,-20,-57,-65,53,23,96,79,87,-12,-18,51,39,-24,27,13,-55,-6,28,95,91,-71,77,49,-26,-17,-83,43,-86,28,20,64,-6,53,40,81,-30,-83,67,-3,25,37,54,95,14,84,-96,76,15,35,41,-86,33,10,-32,59,100,30,-9,58,-80,23,20,43,93,58,-26,37,44,-24,27,99,-46,-80,-85,-44,-45,-72,-32,33,-24,91,-67,75,-40,52,49,94,-10,82,-76,-92,58,18,-43,47,-75,-17,-30,-17,-57,37,51,-32,69,54,-71,-98,-74,-17,99,84,-67,80,-24,-100,98,19,99,-7,-98,-43,73,-97,-21,96,-44,59]
    t_5 = -186

    ret = Solution().threeSumClosest(n_4, t_4)
    print 'sum : %s' %ret