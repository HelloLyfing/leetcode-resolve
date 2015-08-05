<?php

/**
 * minHeap = {'pointer', 'size', 'arr': [minHeapNode, ...]}
 * minHeapNode = {'word': word, 'trieRef': trieRef}
 * trie = {}
 * trieNode = {'count': int, 'headIdx': int, 'isEnd': false, 'child': {trieNode, ...}}
 */
class TopKWordsStat {

    private $minHeapNode = array('word' => NULL, 'trieRef' => NULL);
    private $trieNode = array('count' => 0, 'heapIdx' => -1, 'isEnd' => False, 'children' => array());

    function __construct($top_k) {
        $this->top_k = $top_k;

        $this->minHeap = array('pt' => 0, 'size' => $this->top_k, 'arr' => array());
        $this->trie = array();
        for ($i = 0; $i < $top_k; $i++) {
            // init array
            $this->minHeap['arr'][$i] = NULL;
        }
    }

    private function wordToCode($word) {
        $word = strtolower($word);
        return $word;
    }

    private function swap(&$val1, &$val2) {
        $tmp = $val1;
        $val1 = $val2;
        $val2 = $tmp;
    }

    private function minHeapify($idx) {
        $left = $idx * 2 + 1;
        $right = $idx * 2 + 2;
        $min_idx = $idx;

        $heapNodes = &$this->minHeap['arr'];
        
        if ($left < $this->minHeap['pt'] &&
            $heapNodes[$left]['trieRef']['count'] < $heapNodes[$min_idx]['trieRef']['count']) {
            $min_idx = $left;
        }
        
        if ($right < $this->minHeap['pt'] &&
            $heapNodes[$right]['trieRef']['count'] < $heapNodes[$min_idx]['trieRef']['count']) {
            $min_idx = $right;
        }

        if ($min_idx !== $idx) {
            // switch value
            $this->swap($heapNodes[$min_idx], $heapNodes[$idx]);
            
            // update trieRef->heapIdx
            $heapNodes[$idx]['trieRef']['heapIdx'] = $min_idx;
            $heapNodes[$min_idx]['trieRef']['heapIdx'] = $idx;
            
            $this->minHeapify($min_idx);
        }
    }

    private function rebuildHeap() {
        $n = $this->minHeap['pt'] - 1;
        for ($i = ($n - 1) / 2; $i >= 0; $i--) {
            $this->minHeapify($i);
        }
    }

    private function insertIntoMinHeap($word, &$trie) {
        // 1. word exists
        if ($trie['heapIdx'] > -1) {
            $this->minHeapify($trie['heapIdx']);
        }
        // 2. word no eixsts, heap not full 
        elseif ($this->minHeap['pt'] < $this->minHeap['size']) {
            $pt = $this->minHeap['pt'];
            // 1. update headIdx in trieNode
            $trie['heapIdx'] = $pt;
            // 2. update heapNodeInfo
            $node = &$this->minHeap['arr'][$pt];
            $node['word'] = $word;
            $node['trieRef'] = &$trie;

            $this->minHeap['pt'] += 1;
            $this->rebuildHeap();
        }
        // 3. word no exists, heap is full, word frequency larger than min of minHeap
        elseif ($trie['count'] > $this->minHeap['arr'][0]['trieRef']['count']) {
            $pt = 0;
            // 1. update heapIdx in trieNode
            $trie['heapIdx'] = 0;
            // 2. update heapNodeInfo
            $node = &$this->minHeap['arr'][$pt];
            $node['word'] = $word;
            $node['trieRef'] = &$trie;

            $this->rebuildHeap();
        }
    }

    public function insertAWord($word) {
        $wordCode = $this->wordToCode($word);

        $trie = &$this->trie;
        for ($i = 0; $i < (strlen($wordCode) - 1); $i++) {
            $char = $wordCode[$i];
            if (!isset($trie[$char])) {
                $trie[$char] = $this->trieNode;
            }
            $trie = &$trie[$char]['children'];
        }

        // last character
        $char = $wordCode[strlen($wordCode) - 1];
        if (!isset($trie[$char])) {
            $trie[$char] = $this->trieNode;
        }
        $trie = &$trie[$char];

        if ($trie['isEnd']) {
            $trie['count'] += 1;
        } else {
            $trie['isEnd'] = True;
            $trie['count'] = 1;
        }
        $this->insertIntoMinHeap($word, $trie);
    }

    public function getTopWords() {
        for ($i = 0; $i < $this->top_k; $i++) {
            $backIdx = $this->top_k - 1 - $i;
            $this->swap($this->minHeap['arr'][0], $this->minHeap['arr'][$backIdx]);
            $this->minHeap['pt'] -= 1;
            $this->minHeapify(0);
        }
        
        $arr = array();
        for ($j = 0; $j < $this->top_k; $j++) {
            $node = $this->minHeap['arr'][$j];
            $arr[] = array('word' => $node['word'], 'count' => $node['trieRef']['count']);
        }

        return $arr;
    }
}

/*
$t = '
Welcome to the world of Geeks 
This portal has been created to provide well written well thought and well explained 
solutions for selected questions If you like Geeks for Geeks and would like to contribute 
here is your chance You can write article and mail your article to contribute at 
geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help 
thousands of other Geeks';

$path = 'some-dir/TopKMostFrequentWords.php';
require_once($path);

$stat = new TopKWordsStat(6);

foreach(explode(' ', $t) as $word) {
    $word = trim($word);
    if (empty($word)) continue;    
    
    $stat->insertAWord($word);
}

foreach($stat->getTopWords() as $one) {
    printf('%s (%s)<br>', $one['word'], $one['count']);
}

 */