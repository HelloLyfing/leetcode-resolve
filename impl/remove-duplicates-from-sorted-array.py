class Solution:

    def findInsertPos(self, needle, haystack, start, end):
        if needle == haystack[start] or needle == haystack[end]:
            return None
        if needle > haystack[start]:
            return start
        elif needle < haystack[end]:
            return end + 1

        if start + 1 == end:
            return end
        
        if start + 2 == end:
            if needle == haystack[start + 1]:
                return None
            else:
                return (start + 1) if (needle > haystack[start + 1]) else end
        else:
            avrg = (end - start) / 2
            if needle == haystack[start + avrg]:
                return None

            if needle > haystack[start + avrg]:
                return self.findInsertPos(needle, haystack, start, start + avrg)
            else:
                return self.findInsertPos(needle, haystack, start + avrg + 1, end)

    def rmOne(self, B):
        """Chose the first integer right after 'NULL', try to insert it before 'NULL'"""
        if len(B) >= self.feed_pt + 1:
            i = self.findInsertPos(B[self.feed_pt], B, 0, self.valid_pt)
            if i is not None:
                B.insert(i, B[self.feed_pt])
                self.valid_pt += 1
            self.feed_pt += 1
            return B
        raise Exception('reverse done!')

    def removeDuplicates(self, A):
        self.valid_pt = 0
        self.feed_pt = 1
        if len(A) < 2:
            return len(A)
        
        try:
            while 1: A = self.rmOne(A)
        except Exception:
            pass

        return self.valid_pt + 1
