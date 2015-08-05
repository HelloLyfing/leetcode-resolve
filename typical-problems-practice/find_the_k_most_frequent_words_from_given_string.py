# coding: utf-8

"""
Solution src: http://www.geeksforgeeks.org/find-the-k-most-frequent-words-from-a-file/

Lyfing Comment: This solution is quite clear on how to implement itself, but some method is not well-written.
Like insertAWord(), when I translated the code from c to python, it just went wrong to use 
the original way to implement 'insertAWord', I have to search for the "right way" to implement
a word Trie in python, and finally, it worked.

MinHeap = {'count': 0, 'size': 0, 'arr': [MinHeapNode, ...]}
MinHeapNode: {'word': null, 'trieRef'}
Trie = {}
TrieNode: {'isEnd': false, 'count': null, 'heapIdx': null, 'children': null}
"""

import copy

# these 2 nodes circulate each other
minHeapNode = {'word': None, 'trieRef': None}
trieNode = {'count': 0, 'heapIdx': -1, 'isEnd': None, 'children': {}}

def minHeapify(heap, idx):
    left = idx * 2 + 1
    right = idx * 2 + 2
    min_idx = idx
    
    if left < heap['count'] and \
       heap['arr'][left]['trieRef']['count'] < heap['arr'][min_idx]['trieRef']['count']:
        min_idx = left
    if right < heap['count'] and \
       heap['arr'][right]['trieRef']['count'] < heap['arr'][min_idx]['trieRef']['count']:
        min_idx = right

    if min_idx != idx:
        tmp = heap['arr'][min_idx]
        heap['arr'][min_idx] = heap['arr'][idx]
        heap['arr'][idx] = tmp

        # update trie pointer to a heap item
        heap['arr'][min_idx]['trieRef']['heapIdx'] = idx
        heap['arr'][idx]['trieRef']['heapIdx'] = min_idx

        minHeapify(heap, min_idx)

def buildHeap(heap):
    n = heap['count'] - 1
    i = (n - 1) / 2
    while i >= 0:
        minHeapify(heap, i)
        i = i - 1

def insertIntoHeap(heap, trie, word):
    # 1. word exists
    if trie['heapIdx'] > -1:
        # update the order
        minHeapify(heap, trie['heapIdx'])

    # 2. word not eixsts, heap not full
    elif heap['count'] < heap['size']:
        heap_count = heap['count']
        trie['heapIdx'] = heap_count
        minNode = minHeapNode.copy()
        minNode['word'] = word
        minNode['trieRef'] = trie
        heap['arr'][heap_count] = minNode
        
        heap['count'] += 1
        buildHeap(heap)

    # 3. word not exists, heap is full
    elif trie['count'] > heap['arr'][0]['trieRef']['count']:
        # replace old node
        trie['heapIdx'] = 0
        minNode = minHeapNode.copy()
        minNode['word'] = word
        minNode['trieRef'] = trie
        heap['arr'][0] = minNode
        buildHeap(heap)

def insertAWord(heap, trie, word):
    wordCode = wordToCode(word)

    for i in xrange(len(wordCode) - 1):
        char = wordCode[i]
        if char not in trie:
            trie[char] = copy.deepcopy(trieNode)
        trie = trie[char]['children']

    # last character
    char = wordCode[-1]
    if char not in trie:
        trie[char] = copy.deepcopy(trieNode)
    trie = trie[char]

    if trie['isEnd']:
        trie['count'] += 1
    else:
        trie['isEnd'] = True
        trie['count'] = 1
    
    insertIntoHeap(heap, trie, word)
    
def wordToCode(word):
    '''word (include unicode word) will be transformed into a unique ascii char sequence'''
    word = word.lower()
    return word

def printHeap(heap):
    last = heap['count'] - 1
    
    for i in xrange(heap['count']):
        tmp = heap['arr'][0]
        heap['arr'][0] = heap['arr'][last - i]
        heap['arr'][last - i] = tmp

        heap['count'] -= 1
        buildHeap(heap)

    for i in xrange(last + 1):
        item = heap['arr'][i]
        print 'count: %s, word: %s' %(item['trieRef']['count'], item['word'])

if __name__ == '__main__':
    text = '''
    Welcome to the world of Geeks 
    This portal has been created to provide well written well thought and well explained 
    solutions for selected questions If you like Geeks for Geeks and would like to contribute 
    here is your chance You can write article and mail your article to contribute at 
    geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help 
    thousands of other Geeks
    '''
    
    top_k = 11
    trie = {}
    heap = {'count': 0, 'size': top_k, 'arr': [None for i in range(top_k)]}
    
    for word in [t.strip() for t in text.split(' ')]:
        if not word: continue
        insertAWord(heap, trie, word)
    
    printHeap(heap)
    