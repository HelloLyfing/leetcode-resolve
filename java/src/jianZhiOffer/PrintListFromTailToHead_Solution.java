package jianZhiOffer;

import utils.LogUtils;

import java.util.ArrayList;
import java.util.Stack;

public class PrintListFromTailToHead_Solution {

    public static ArrayList<Integer> printListFromTailToHead_Stack(ListNode listNode) {
        if (listNode == null) {
            return new ArrayList<>();
        }

        Stack<Integer> stack = new Stack<>();

        ListNode node = listNode;
        while (node != null) {
            stack.push(node.val);
            node = node.next;
        }

        ArrayList<Integer> arrayList = new ArrayList<>(stack.size());
        while (!stack.isEmpty()) {
            arrayList.add(stack.pop());
        }
        return arrayList;
    }

    public static ArrayList<Integer> printListFromTailToHead_Recursive(ListNode listNode) {
        if (listNode == null) {
            return new ArrayList<>();
        }

        ArrayList<Integer> arrayList = new ArrayList<>();
        getItemFromRecursive(arrayList, listNode);
        return arrayList;
    }

    private static void getItemFromRecursive(ArrayList<Integer> arrayList, ListNode listNode) {
        if (listNode.next != null) {
            getItemFromRecursive(arrayList, listNode.next);
        }
        arrayList.add(listNode.val);
    }

    private static class ListNode {
         int val;
         ListNode next = null;
         ListNode(int val) {
             this.val = val;
         }
    }

    public static void main(String[] args) {
        ListNode node = new ListNode(-1);
        ListNode idx = node;
        for (int i = 0; i < 10; i++) {
            idx.next = new ListNode(i + 1);
            idx = idx.next;
        }

        LogUtils.info(printListFromTailToHead_Stack(node));
        LogUtils.info(printListFromTailToHead_Recursive(node));
    }
}