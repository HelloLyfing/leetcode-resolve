package jianZhiOffer;

/**
 * 面试题3：二维数组中的查找
 */
public class Array_Find_Solution {

    public boolean Find(int target, int [][] array) {
        if (array == null || array.length == 0 || array[0].length == 0) {
            return false;
        }

        int hIdx = 0, lIdx = array[0].length - 1;
        int val;
        while (true) {
            val = array[hIdx][lIdx];
            if (val == target) {
                return true;
            }
            if (val < target) {
                hIdx += 1;
                if (hIdx > array.length - 1) {
                    break;
                }
            } else if (val > target) {
                lIdx -= 1;
                if (lIdx < 0) {
                    break;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) {

    }

}