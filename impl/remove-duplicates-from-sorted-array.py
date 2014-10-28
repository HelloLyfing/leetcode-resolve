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
        """
        valid_pt is pointting at the last valid item,
        while feed_pt will traverse all items except the first one(B[1:])
        """
        if len(B) >= self.feed_pt + 1:
            i = self.findInsertPos(B[self.feed_pt], B, 0, self.valid_pt)
            if i is not None:
                B.insert(i, B[self.feed_pt])
                self.valid_pt += 1
            self.feed_pt += 1
            return B
        raise Exception('traverse done!')

    def removeDuplicatesUnsorted(self, A):
        """use this method to remove duplicated item from unsorted array"""
        if len(A) < 2:
            return len(A)
        
        self.valid_pt = 0
        self.feed_pt = 1
        try:
            while 1: A = self.rmOne(A)
        except Exception:
            pass

        return self.valid_pt + 1

    def removeDuplicates(self, A):
        lenA = len(A)

        if lenA < 2: return lenA

        valid_pt = 0
        feed_pt = 1
        while (feed_pt + 1) <= lenA:
            if A[valid_pt] == A[feed_pt]:
                feed_pt += 1
                continue

            valid_pt += 1
            A[valid_pt] = A[feed_pt]
            feed_pt += 1

        return valid_pt + 1
