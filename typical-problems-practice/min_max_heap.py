# coding: utf-8

class BaseHeap(object):

    num_arr = None

    def __init__(self, num_arr):
        self.num_arr = [None for i in num_arr]
        # build up the min/max heap
        self.num_arr[0] = num_arr[0]
        for i in xrange(1, len(num_arr)):
            self.append_to_end(i, num_arr[i])
    
    def get(self, idx):
        return self.num_arr[idx]

    def set(self, idx, val):
        self.num_arr[idx] = val

    def get_p_idx(self, node_idx):
        """get parent node index by given node index"""
        idx = (node_idx + 1) / 2 - 1
        return idx
    
    def get_c_idx(self, node_idx):
        """get child node index by given node index"""
        idx = (node_idx + 1) * 2 - 1
        return idx

    def get_plain_arr(self):
        return self.num_arr

class MinHeap(BaseHeap):

    def append_to_end(self, i, val):
        n_idx = i
        p_idx = self.get_p_idx(n_idx)
        while p_idx >= 0:
            if val > self.get(p_idx):
                break

            self.set(n_idx, self.get(p_idx))
            n_idx = p_idx
            p_idx = self.get_p_idx(n_idx)
        
        self.set(n_idx, val)

    def drop_from_top(self, val, n):
        n_idx = 0
        c_idx = self.get_c_idx(n_idx)

        while c_idx <= n:
            if c_idx + 1 <= n and self.get(c_idx + 1) < self.get(c_idx):
                c_idx += 1
                
            if val <= self.get(c_idx):
                break
            self.set(n_idx, self.get(c_idx))
            n_idx = c_idx
            c_idx = self.get_c_idx(n_idx)

        self.set(n_idx, val)

class MaxHeap(BaseHeap):
    
    def append_to_end(self, i, val):
        n_idx = i
        p_idx = self.get_p_idx(n_idx)
        while p_idx >= 0:
            if val <= self.get(p_idx):
                break

            self.set(n_idx, self.get(p_idx))
            n_idx = p_idx
            p_idx = self.get_p_idx(n_idx)

        self.set(n_idx, val)

    def drop_from_top(self, val, n):
        n_idx = 0
        c_idx = self.get_c_idx(n_idx)
        while c_idx <= n:
            if c_idx + 1 <= n and self.get(c_idx) < self.get(c_idx + 1):
                c_idx += 1
            
            if val >= self.get(c_idx):
                break

            self.set(n_idx, self.get(c_idx))
            n_idx = c_idx
            c_idx = self.get_c_idx(n_idx)

        self.set(n_idx, val)    

if __name__ == '__main__':
    num_arr = [1, 10, 0, -1, 8, 5, -4, 88, 97, -23, 2, -3, 100, -99, 27, 10]
    num_len = len(num_arr)
    min_heap = MinHeap(num_arr)
    max_heap = MaxHeap(num_arr)

    print min_heap.get_plain_arr()
    for i in xrange(num_len):
        min_now = min_heap.get(0)
        tmp_val = min_heap.get(num_len - 1 - i)
        min_heap.set(num_len - 1 - i, min_now)
        min_heap.drop_from_top(tmp_val, num_len - 1 - i - 1)
    print 'MinHeap : %s' %min_heap.get_plain_arr()

    print max_heap.get_plain_arr()
    for i in xrange(num_len):
        max_now = max_heap.get(0)
        tmp_val = max_heap.get(num_len - 1 - i)
        max_heap.set(num_len - 1 - i, max_now)
        max_heap.drop_from_top(tmp_val, num_len - 1 - i - 1)
    print 'MaxHeap : %s' %max_heap.get_plain_arr()