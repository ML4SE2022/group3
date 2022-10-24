public class Solution {
    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        String[] units = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        String[] tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        String[] thousands = {"", "Thousand", "Million", "Billion"};
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (num > 0) {
            if (num % 1000 != 0) {
                sb.insert(0, thousands[i] + " ");
                int h = num % 10;
                int t = (num % 100) / 10;
                int u = (num % 1000) / 100;
                if (t == 1) {
                    sb.insert(0, units[t * 10 + h] + " ");
                } else {
                    if (h != 0) sb.insert(0, units[h] + " ");
                    if (t != 0) sb.insert(0, tens[t] + " ");
                }
                if (u != 0) sb.insert(0, units[u] + " Hundred ");
            }
            num /= 1000;
            i++;
        }
        return sb.toString().trim();
    }
}