class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        max_idx = max(len(ver1), len(ver2))

        for i in xrange(max_idx):
            if i >= len(ver1):
                sub_ver1 = 0
            else:
                sub_ver1 = int(ver1[i])
            if i >= len(ver2):
                sub_ver2 = 0
            else:
                sub_ver2 = int(ver2[i])
            
            val = sub_ver1 - sub_ver2
            if val == 0:
                continue
            return 1 if val > 0 else -1
        
        return 0

if __name__ == '__main__':
    list = [('1.3.2', '1.3.1'), ('21.0.0', '21.0.16'), ('2.0', '2'), ('3.0.1', '3.0.0')]
    for tupl in list:
        print '%s = %s' %(tupl, Solution().compareVersion(*tupl))
