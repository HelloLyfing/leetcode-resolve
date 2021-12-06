class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if haystack == needle or len(needle) == 0:
            return haystack
        if len(needle) > len(haystack):
            return None

        n_len = len(needle)
        # where to restart match procedure
        start_pt = 0
        # count matched len
        match_len = None
        while start_pt + n_len <= len(haystack):
            # let's take a step walk one by one
            step_pt = 0
            match_len = 0
            while (step_pt + 1) <= n_len and \
                  needle[step_pt] == haystack[start_pt + step_pt]:
                step_pt += 1
                match_len += 1

            if match_len == n_len:
                break
            start_pt += 1
        return haystack[start_pt:] if (match_len == n_len) else None
