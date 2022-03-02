package common;

import utils.LogUtils;

import java.util.Arrays;

/**
 * @author dongxu.lu
 * @date 2021/12/21
 */
public class SortingCollection {

    /**
     * 快速排序，时间效率同为O(N*logN)的几种排序方法中效率较高，因此经常被采用，快速排序思想的分治法也确实实用
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

    /**
     * 归并排序，时间复杂度：O(nlogn), 空间复杂度O(n)
     * 核心过程：脑子里记下归并排序的图
     */
    static class MergeSortRecurse {

        public static void sortAndMerge(int[] origArr, int tempArr[], int beginIdx, int endIdx) {
            if (beginIdx < endIdx) {
                int middle = (beginIdx + endIdx) / 2;
                sortAndMerge(origArr, tempArr, beginIdx, middle);
                sortAndMerge(origArr, tempArr, middle + 1, endIdx);
                merge(origArr, tempArr, beginIdx, middle, endIdx);
            }
        }

        public static void merge(int[] origArr, int tempArr[], int beginIdx, int midIdx, int endIdx) {
            int i = beginIdx, j = midIdx + 1;
            int t = 0;
            while (i <= midIdx && j <= endIdx) {
                if (origArr[i] < origArr[j]) {
                    tempArr[t++] = origArr[i++];
                } else {
                    tempArr[t++] = origArr[j++];
                }
            }

            while (i <= midIdx) {
                tempArr[t++] = origArr[i++];
            }
            while (j <= endIdx) {
                tempArr[t++] = origArr[j++];
            }

            // 把暂存的tempArr排序结果，反哺至原数组
            t = 0;
            while (beginIdx <= endIdx) {
                origArr[beginIdx++] = tempArr[t++];
            }
        }
    }

    public static void main(String[] args) {
        int[] simpleArr = new int[] {10, 5, 0, 2, 3, 9, 6, 8, 4, 7, 0, 1};

        int[] arr1 = copyArray(simpleArr);
        quickSort(arr1, 0, arr1.length - 1);
        LogUtils.info("quickSort", arr1);

        int[] arr2 = copyArray(simpleArr);
        MergeSortRecurse.sortAndMerge(arr2, new int[arr2.length], 0, arr2.length - 1);
        LogUtils.info("mergeSort", arr2);

    }

    private static int[] copyArray(int[] simpleArr) {
        return Arrays.copyOf(simpleArr, simpleArr.length);
    }

}