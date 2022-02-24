package jianZhiOffer;

import java.util.Stack;

/**
 * 用两个栈实现一个队列
 * 发散：用两个队列实现一个栈
 */
public class TwoStack_To_Queue {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();

    public void push(int node) {
        while (!stack2.isEmpty()) {
            stack1.add(stack2.pop());
        }
        stack1.push(node);
    }

    public int pop() {
        while (!stack1.isEmpty()) {
            stack2.add(stack1.pop());
        }
        return stack2.pop();
    }

    public static void main(String[] args) {

    }

}