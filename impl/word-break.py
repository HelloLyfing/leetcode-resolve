class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak_1(self, s, part_arr):
        def recurse(s, part_arr, start):
            # the final match, start succefully walks to the end of the s
            if start == len(s):
                return True

            for part in part_arr:
                end = start + len(part)
                # the <end> has already reached out of s's length, will be ingore
                if end > len(s):
                    continue

                if s[start:end] == part and recurse(s, part_arr, end):
                    return True

            return False

        return recurse(s, part_arr, 0)

t1 = ('cars', ["car","ca","rs"])
t2 = ("aaaaaaa", ["aaaa","aaa"])
t3 = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print Solution().wordBreak_1(*t3)