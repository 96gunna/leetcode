import java.util.ArrayList;
import java.util.List;

class encodeDecodeStr {
    public static String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        // Store the length of the string and an escape character before the actual string
        for (String string : strs) {
            sb.append(string.length()).append("~").append(string);
        }
        return sb.toString();
    }

    public static List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        // Two pointer approach
        int i = 0;
        while (i < str.length()) {
            int j = i;
            // Move along j index until the escape character
            while (str.charAt(j) != '~') j++;
            // Encoded length of the string is between the indices i and j
            int length = Integer.parseInt(str.substring(i, j++));
            // Place i index at the end of the current string
            i = j + length;
            // Add substring to the list
            result.add(str.substring(j, i));
        }
        return result;
    }
}
//     The overcomplicated initial approach for decoding
//        for (int i = 0; i < str.length(); i++) {
//            StringBuilder sb = new StringBuilder();
//            while (str.charAt(i) != '~') {
//                sb.append(str.charAt(i++));
//            }
//            int currLen = Integer.parseInt(sb.toString());
//            int j = ++i + currLen;
//            result.add(str.substring(i, j));
//            i = j - 1;
//        }
