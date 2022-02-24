package utils;

import com.google.gson.Gson;

/**
 * @author dongxu.lu
 * @date 2021/12/20
 */
public class LogUtils {

    private static final Gson GSON = genGSON();

    private static Gson genGSON() {
        Gson gson = new Gson();
        return gson;
    }

    public static void info(Object... objects) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < objects.length; i++) {
            if (i > 0) {
                sb.append(" | ");
            }
            sb.append(toJSONString(objects[i]));
        }
        System.out.println(sb);
    }

    private static String toJSONString(Object object) {
        if (object instanceof String || object instanceof Number) {
            return String.valueOf(object);
        }

        return GSON.toJson(object);
    }

    public static void printLine() {
        System.out.println("--------------------------");
    }

}
