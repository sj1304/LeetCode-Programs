import java.util.Hashtable;

class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        Hashtable<Character, Integer> ht = new Hashtable<>();

        // Count characters in s
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (!ht.containsKey(ch)) {
                ht.put(ch, 1);
            } else {
                ht.put(ch, ht.get(ch) + 1);
            }
        }

        // Remove characters using t
        for (int i = 0; i < t.length(); i++) {
            char ch = t.charAt(i);

            if (!ht.containsKey(ch)) {
                return false;
            }

            int count = ht.get(ch);

            if (count == 1) {
                ht.remove(ch);
            } else {
                ht.put(ch, count - 1);
            }
        }

        return ht.isEmpty();
    }
}