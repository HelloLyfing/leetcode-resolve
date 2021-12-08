class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum_old(self, nums, sum_need):
        self.final = []

        nums = sorted(nums)
        if len(nums) == 0:
            return self.final
        nums_len = len(nums)
        exist_comb = []

        for i in xrange(len(nums) - 4):
            for j in xrange(i + 1, len(nums) - 3):
                x = j + 1
                y = len(nums) - 1
                while x < y:
                    tmp = (nums[i], nums[j], nums[x], nums[y])
                    tmp_sum = sum(tmp)
                    if tmp_sum > sum_need:
                        y -= 1
                    elif tmp_sum < sum_need:
                        x += 1
                    elif tmp_sum == sum_need:
                        pos_code = '%s%s%s%s' %(i, j, x, y)
                        if pos_code in exist_comb:
                            continue
                        
                        exist_comb.append(pos_code)
                        self.final.append(tmp)
                        break
        
        return self.final

    def fourSum(self, nums, sum_need):
        nums_len = len(nums)
        if nums_len < 4:
            return []

        nums = sorted(nums)
        if nums_len == 4:
            return [nums] if sum(nums) == sum_need else []

        _2comb_d = {}
        for a in xrange(nums_len - 1):
            for b in xrange(a + 1, nums_len):
                tmp_sum = nums[a] + nums[b]
                if tmp_sum in _2comb_d:
                    _2comb_d[tmp_sum].append((a,b))
                else:
                    _2comb_d[tmp_sum] = [(a,b)]

        pos4_set = set()
        for i in xrange(nums_len - 1):
            for j in xrange(i + 1, nums_len):
                left = sum_need - nums[i] - nums[j]
                if _2comb_d.get(left):
                    for pos_tp in _2comb_d[left]:
                        if pos_tp[0] > j:
                            pos4_set.add((nums[i], nums[j], nums[pos_tp[0]], nums[pos_tp[1]]))

        return [list(x) for x in pos4_set]
        
if __name__ == '__main__':
    n_1 = [1, 0, -1, 0, -2, 2]
    t_1 = 0

    n_2 = [91277418,66271374,38763793,4092006,11415077,60468277,1122637,72398035,-62267800,22082642,60359529,-16540633,92671879,-64462734,-55855043,-40899846,88007957,-57387813,-49552230,-96789394,18318594,-3246760,-44346548,-21370279,42493875,25185969,83216261,-70078020,-53687927,-76072023,-65863359,-61708176,-29175835,85675811,-80575807,-92211746,44755622,-23368379,23619674,-749263,-40707953,-68966953,72694581,-52328726,-78618474,40958224,-2921736,-55902268,-74278762,63342010,29076029,58781716,56045007,-67966567,-79405127,-45778231,-47167435,1586413,-58822903,-51277270,87348634,-86955956,-47418266,74884315,-36952674,-29067969,-98812826,-44893101,-22516153,-34522513,34091871,-79583480,47562301,6154068,87601405,-48859327,-2183204,17736781,31189878,-23814871,-35880166,39204002,93248899,-42067196,-49473145,-75235452,-61923200,64824322,-88505198,20903451,-80926102,56089387,-58094433,37743524,-71480010,-14975982,19473982,47085913,-90793462,-33520678,70775566,-76347995,-16091435,94700640,17183454,85735982,90399615,-86251609,-68167910,-95327478,90586275,-99524469,16999817,27815883,-88279865,53092631,75125438,44270568,-23129316,-846252,-59608044,90938699,80923976,3534451,6218186,41256179,-9165388,-11897463,92423776,-38991231,-6082654,92275443,74040861,77457712,-80549965,-42515693,69918944,-95198414,15677446,-52451179,-50111167,-23732840,39520751,-90474508,-27860023,65164540,26582346,-20183515,99018741,-2826130,-28461563,-24759460,-83828963,-1739800,71207113,26434787,52931083,-33111208,38314304,-29429107,-5567826,-5149750,9582750,85289753,75490866,-93202942,-85974081,7365682,-42953023,21825824,68329208,-87994788,3460985,18744871,-49724457,-12982362,-47800372,39958829,-95981751,-71017359,-18397211,27941418,-34699076,74174334,96928957,44328607,49293516,-39034828,5945763,-47046163,10986423,63478877,30677010,-21202664,-86235407,3164123,8956697,-9003909,-18929014,-73824245]
    t_2 = -236727523

    n_3 = [0, 0, 0, 0]
    t_3 = 0

    n_4 = [-1,0,1,2,-1,-4]
    t_4 = -1

    n_5 = [-3,-2,-1,0,0,1,2,3] 
    t_5 = 0

    import time
    print 'time:%s' %int(time.time())
    ret = Solution().fourSum(n_5, t_5)
    print 'time:%s' %int(time.time())
    for comb in ret:
        print comb