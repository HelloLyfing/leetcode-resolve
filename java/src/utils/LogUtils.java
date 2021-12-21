package utils;

import com.google.gson.Gson;

/**
 * @author dongxu.lu
 * @date 2021/12/20
 */
public class LogUtils {

    private static final Gson GSON = new Gson();

    public static void info(Object object) {
        System.out.println(GSON.toJson(object));
    }

}
