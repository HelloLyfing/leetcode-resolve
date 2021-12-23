package common;

import utils.LogUtils;

import java.util.ArrayList;

/**
 * 给定一棵二叉树，分别按照二叉树先序，中序和后序打印所有的节点
 * @author dongxu.lu
 * @date 2021/12/21
 */
public class BinaryTree_Traverse_Solution {

    /**
     *
     * @param node TreeNode类 the node of binary tree
     * @return int整型二维数组
     */
    public static int[][] threeOrders (TreeNode node) {
        ArrayList<Integer> arrList1 = new ArrayList<>();

        if (node != null) {
            preOrders_Recurse(arrList1, node);
        }

        ArrayList<Integer> arrList2 = new ArrayList<>();
        if (node != null) {
            middleOrders_Recurse(arrList2, node);
        }

        ArrayList<Integer> arrList3 = new ArrayList<>();
        if (node != null) {
            afterOrders_Recurse(arrList3, node);
        }

        int[][] result = new int[3][arrList1.size()];
        for (int i = 0; i < arrList1.size(); i++) {
            result[0][i] = arrList1.get(i);
            result[1][i] = arrList2.get(i);
            result[2][i] = arrList3.get(i);
        }

        return result;
    }

    private static void preOrders_Recurse(ArrayList<Integer> intArr, TreeNode node) {
        intArr.add(node.val);

        if (node.left != null) {
            preOrders_Recurse(intArr, node.left);
        }
        if (node.right != null) {
            preOrders_Recurse(intArr, node.right);
        }
    }

    private static void middleOrders_Recurse(ArrayList<Integer> intArr, TreeNode node) {
        if (node.left != null) {
            middleOrders_Recurse(intArr, node.left);
        }

        intArr.add(node.val);

        if (node.right != null) {
            middleOrders_Recurse(intArr, node.right);
        }
    }

    private static void afterOrders_Recurse(ArrayList<Integer> intArr, TreeNode node) {
        if (node.left != null) {
            afterOrders_Recurse(intArr, node.left);
        }

        if (node.right != null) {
            afterOrders_Recurse(intArr, node.right);
        }

        intArr.add(node.val);
    }


    public static void addLeftRightNodes(TreeNode node, int level) {
        if (level > 3) {
            return;
        }
        node.val = level * 10 + 1;

        node.left = new TreeNode();
        node.left.val = level * 10 + 3;

        node.right = new TreeNode();
        node.right.val = level * 10 + 5;

        addLeftRightNodes(node.left, level + 1);
        addLeftRightNodes(node.right, level + 1);
    }

    private static class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;
    }


    public static void main(String[] args) {
        TreeNode node = new TreeNode();
        addLeftRightNodes(node, 1);

        int[][] result = threeOrders(node);
        LogUtils.info(result);

        result = threeOrders(null);
        LogUtils.info(result);


        node = new TreeNode();
        node.val = 1;
        result = threeOrders(node);
        LogUtils.info(result);
    }

}