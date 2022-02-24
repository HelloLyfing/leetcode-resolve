package common;

import utils.LogUtils;

/**
 * 斐波那切数列相关研究
 * @author luyu
 * @date 2022/2/24
 */
public class FibonacciCollection {

    /**
     * f(n) =
     * n = 0, f(n) = 0;
     * n = 1, f(n) = 1;
     * n > 1, f(n) = f(n-1) + f(n-2)
     */
    public static int fibonacci_Recurse(int input) {
        if (input == 0) {
            return 0;
        } else if (input == 1) {
            return 1;
        }
        return fibonacci_Recurse(input - 1) + fibonacci_Recurse(input - 2);
    }

    /**
     * 通过循环的方式计算斐波那切数列
     * 核心概要：f(n) = f(n-1) + f(n-2)，n-1和n-2的值可以暂存起来为下一步所用
     */
    public static int fibonacci_Loop(int input) {
        if (input == 0) {
            return 0;
        } else if (input == 1) {
            return 1;
        }

        int minus1 = 1;
        int minus2 = 0;
        int currVal = 0;
        for (int n = 2; n <= input;) {
            currVal = minus1 + minus2;

            n++;
            minus2 = minus1;
            minus1 = currVal;
        }

        return currVal;
    }

    public static void main(String[] args) {
        for (int i = 0; i < 20; i++) {
            LogUtils.info(
                    "current->" + i +
                    ", recurse->" + fibonacci_Recurse(i) +
                    ", loop->" + fibonacci_Loop(i));
        }
    }

}