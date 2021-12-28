package utils;

import com.google.gson.Gson;

/**
 * @author dongxu.lu
 * @date 2021/12/20
 */
public class LogUtils {

    private static final Gson GSON = new Gson();

    public static void info(Object... objects) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < objects.length; i++) {
            if (i > 0) {
                sb.append(" | ");
            }
            sb.append(GSON.toJson(objects[i]));
        }
        System.out.println(sb);
    }

    public static void printLine() {
        System.out.println("--------------------------");
    }

}
