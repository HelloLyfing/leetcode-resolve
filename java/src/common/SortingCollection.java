package common;

import utils.LogUtils;

/**
 * 给定一棵二叉树，分别按照二叉树先序（根左右），中序（左根右）和后序（左右根）打印所有的节点
 * 薄弱点：用栈数据结构模拟递归调用方面较弱
 * @author dongxu.lu
 * @date 2021/12/21
 */
public class SortingCollection {

    /**
     * 快速排序由于排序效率在同为O(N*logN)的几种排序方法中效率较高，因此经常被采用，快速排序思想的分治法也确实实用
     *
     * 核心过程：
     * 阶段1：挖坑暂存A，找新值填充老坑，到i=j时归还暂存的A
     * 阶段2：将A一分为2，左边部分、右边部分重复阶段1
     *
     * 从数组随机选择一个数，比如第一个数
     * 使用loop的方式从后往前找，直到找到<=A的，挖走填上一步坑；
     * 使用loop的方式从前往后找，找到>A的，挖走填上一步坑；
     * 直到i=j，将暂存的A归还给位置i的坑位
     */
    public static void quickSort(int[] argArr, int beginIdx, int endIdx) {
        if (argArr == null || argArr.length < 1) {
            return;
        }

        if (beginIdx >= endIdx) {
            return;
        }

        int tempVal = argArr[beginIdx];
        int i = beginIdx, j = endIdx;

        while (i < j) {
            while (i < j) {
                if (argArr[j] < tempVal) {
                    argArr[i] = argArr[j];
                    break;
                } else {
                    j--;
                }
            }

            while (i < j) {
                if (argArr[i] > tempVal) {
                    argArr[j] = argArr[i];
                    break;
                } else {
                    i++;
                }
            }
        }
        argArr[i] = tempVal;

        quickSort(argArr, beginIdx, i - 1);
        quickSort(argArr, i + 1, endIdx);
    }

    public static void main(String[] args) {
        int[] simpleArr = new int[] {10, 5, 0, 2, 3, 9, 6, 8, 4, 7, 0, 1};
        quickSort(simpleArr, 0, simpleArr.length - 1);

        LogUtils.info(simpleArr);
    }

}