package common;

import utils.LogUtils;

import java.util.ArrayList;
import java.util.Random;
import java.util.Stack;

/**
 * 给定一棵二叉树，分别按照二叉树先序（根左右），中序（左根右）和后序（左右根）打印所有的节点
 * 薄弱点：用栈数据结构模拟递归调用方面较弱
 * @author dongxu.lu
 * @date 2021/12/21
 */
public class BinaryTree_Traverse_Solution {

    private static final Random RANDOM = new Random(System.currentTimeMillis());

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
            postOrders_Recurse(arrList3, node);
        }

        int[][] result = new int[3][arrList1.size()];
        for (int i = 0; i < arrList1.size(); i++) {
            result[0][i] = arrList1.get(i);
            result[1][i] = arrList2.get(i);
            result[2][i] = arrList3.get(i);
        }

        return result;
    }

    /**
     * 前序遍历，根左右，
     * 效果为：
     */
    private static void preOrders_Recurse(ArrayList<Integer> arrList, TreeNode node) {
        arrList.add(node.val);

        if (node.left != null) {
            preOrders_Recurse(arrList, node.left);
        }
        if (node.right != null) {
            preOrders_Recurse(arrList, node.right);
        }
    }

    private static void preOrders_OnStack(ArrayList<Integer> arrList, TreeNode node) {
        if (node == null) {
            return;
        }

        Stack<TreeNode> stack = new Stack<>();
        stack.add(node);

        TreeNode currNode;
        while (!stack.isEmpty()) {
            currNode = stack.pop();
            arrList.add(currNode.val);

            if (currNode.right != null) {
                stack.add(currNode.right);
            }

            if (currNode.left != null) {
                stack.add(currNode.left);
            }
        }
    }

    private static void middleOrders_Recurse(ArrayList<Integer> arrList, TreeNode node) {
        if (node.left != null) {
            middleOrders_Recurse(arrList, node.left);
        }

        arrList.add(node.val);

        if (node.right != null) {
            middleOrders_Recurse(arrList, node.right);
        }
    }

    private static void middleOrders_OnStack(ArrayList<Integer> arrList, TreeNode node) {
        if (node == null) {
            return;
        }

        Stack<TreeNode> stack = new Stack<>();
        TreeNode currNode = node;
        while (!stack.isEmpty() || currNode != null) {
            while (currNode != null) {
                stack.add(currNode);
                currNode = currNode.left;
            }

            currNode = stack.pop();
            arrList.add(currNode.val);

            currNode = currNode.right;
        }
    }

    private static void postOrders_Recurse(ArrayList<Integer> arrList, TreeNode node) {
        if (node.left != null) {
            postOrders_Recurse(arrList, node.left);
        }

        if (node.right != null) {
            postOrders_Recurse(arrList, node.right);
        }

        arrList.add(node.val);
    }

    private static void postOrders_OnStack(ArrayList<Integer> arrList, TreeNode node) {
        if (node == null) {
            return;
        }

        Stack<TreeNode> stack = new Stack<>();
        stack.push(node);

        TreeNode currNode = null, preNode = null;
        while (!stack.isEmpty()) {
            currNode = stack.peek();

            if ((currNode.left == null && currNode.right == null) // 叶子节点
                    || (preNode != null && currNode.left == preNode || currNode.right == preNode)) { // 叶子节点的parent
                arrList.add(currNode.val);
                preNode = stack.pop();
            } else {
                if (currNode.right != null) {
                    stack.push(currNode.right);
                }
                if (currNode.left != null) {
                    stack.push(currNode.left);
                }
            }
        }
    }

    public static void addLeftRightNodes(TreeNode node, int level) {
        if (level > 3) {
            return;
        }
        node.val = level * 10 + 1;

        node.left = new TreeNode();
        node.left.val = level * 20 + RANDOM.nextInt(10);

        node.right = new TreeNode();
        node.right.val = level * 30 + RANDOM.nextInt(10);

        addLeftRightNodes(node.left, level + 1);
        addLeftRightNodes(node.right, level + 1);
    }

    private static class TreeNode {
        int val = 0;
        TreeNode left = null;
        TreeNode right = null;
    }


    public static void main(String[] args) {
        TreeNode node;
        ArrayList<Integer> arrList;

        node = new TreeNode();
        addLeftRightNodes(node, 1);

        arrList = new ArrayList<>();
        preOrders_Recurse(arrList, node);
        LogUtils.info("preOrders_Recurse", arrList);

        arrList = new ArrayList<>();
        preOrders_OnStack(arrList, node);
        LogUtils.info("preOrders_OnStack", arrList);

        LogUtils.printLine();
        arrList = new ArrayList<>();
        middleOrders_Recurse(arrList, node);
        LogUtils.info("middleOrders_Recurse", arrList);

        arrList = new ArrayList<>();
        middleOrders_OnStack(arrList, node);
        LogUtils.info("middleOrders_OnStack", arrList);

        LogUtils.printLine();
        arrList = new ArrayList<>();
        postOrders_Recurse(arrList, node);
        LogUtils.info("postOrders_Recurse", arrList);

        arrList = new ArrayList<>();
        postOrders_OnStack(arrList, node);
        LogUtils.info("postOrders_OnStack", arrList);

        LogUtils.printLine();
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