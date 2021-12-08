package jianZhiOffer;

public class String_ReplaceSpace_Solution {

    /**
     */
    public static String replaceSpace(String input) {
        if (input == null || input.isEmpty()) {
            return input;
        }

        char spaceChar = " ".charAt(0);
        int spaceCount = 0;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == spaceChar) {
                spaceCount += 1;
            }
        }

        if (spaceCount == 0) {
            return input;
        }

        char[] newArr = new char[input.length() + spaceCount * 2];
        int newIdx = 0;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == spaceChar) {
                newArr[newIdx++] = '%';
                newArr[newIdx++] = '2';
                newArr[newIdx++] = '0';
            } else {
                newArr[newIdx++] = input.charAt(i);
            }
        }
        return new String(newArr);
    }

    public static void main(String[] args) {
        String input = "hello world ! ";
        System.out.println(replaceSpace(input));
    }

}