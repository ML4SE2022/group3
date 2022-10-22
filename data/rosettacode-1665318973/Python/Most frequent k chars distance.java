import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;


public class SDF {

    /** Counting the number of occurrences of each character
     * @param character array
     * @return hashmap : Key = char, Value = num of occurrence
     */
    public static HashMap<Character, Integer> countElementOcurrences(char[] array) {

        HashMap<Character, Integer> countMap = new HashMap<Character, Integer>();

        for (char element : array) {
            Integer count = countMap.get(element);
            count = (count == null) ? 1 : count + 1;
            countMap.put(element, count);
        }

        return countMap;
    }
    
    /**
     * Sorts the counted numbers of characters (keys, values) by java Collection List
     * @param HashMap (with key as character, value as number of occurrences)
     * @return sorted HashMap
     */
    private static <K, V extends Comparable<? super V>>
            HashMap<K, V> descendingSortByValues(HashMap<K, V> map) { 
	List<Map.Entry<K, V>> list = new ArrayList<Map.Entry<K, V>>(map.entrySet());
	// Defined Custom Comparator here
	Collections.sort(list, new Comparator<Map.Entry<K, V>>() {
		public int compare(Map.Entry<K, V> o1, Map.Entry<K, V> o2) {
		    return o2.getValue().compareTo(o1.getValue());
		}
	    });

	// Here I am copying the sorted list in HashMap
	// using LinkedHashMap to preserve the insertion order
	HashMap<K, V> sortedHashMap = new LinkedHashMap<K, V>();
	for (Map.Entry<K, V> entry : list) {
	    sortedHashMap.put(entry.getKey(), entry.getValue());
	} 
	return sortedHashMap;
    }
    /**
     * get most frequent k characters
     * @param array of characters
     * @param limit of k
     * @return hashed String 
     */
    public static String mostOcurrencesElement(char[] array, int k) {
        HashMap<Character, Integer> countMap = countElementOcurrences(array);
        System.out.println(countMap);
        Map<Character, Integer> map = descendingSortByValues(countMap); 
        System.out.println(map);
        int i = 0;
        String output = "";
        for (Map.Entry<Character, Integer> pairs : map.entrySet()) {
	    if (i++ >= k)
		break;
            output += "" + pairs.getKey() + pairs.getValue();
        }
        return output;
    }
    /**
     * Calculates the similarity between two input strings
     * @param input string 1
     * @param input string 2
     * @param maximum possible limit value 
     * @return distance as integer
     */
    public static int getDiff(String str1, String str2, int limit) {
        int similarity = 0;
	int k = 0;
	for (int i = 0; i < str1.length() ; i = k) {
	    k ++;
	    if (Character.isLetter(str1.charAt(i))) {
		int pos = str2.indexOf(str1.charAt(i));
				
		if (pos >= 0) {	
		    String digitStr1 = "";
		    while ( k < str1.length() && !Character.isLetter(str1.charAt(k))) {
			digitStr1 += str1.charAt(k);
			k++;
		    }
					
		    int k2 = pos+1;
		    String digitStr2 = "";
		    while (k2 < str2.length() && !Character.isLetter(str2.charAt(k2)) ) {
			digitStr2 += str2.charAt(k2);
			k2++;
		    }
					
		    similarity += Integer.parseInt(digitStr2)
			+ Integer.parseInt(digitStr1);
					
		} 
	    }
	}
	return Math.abs(limit - similarity);
    }
    /**
     * Wrapper function 
     * @param input string 1
     * @param input string 2
     * @param maximum possible limit value 
     * @return distance as integer
     */
    public static int SDFfunc(String str1, String str2, int limit) {
        return getDiff(mostOcurrencesElement(str1.toCharArray(), 2), mostOcurrencesElement(str2.toCharArray(), 2), limit);
    }

    public static void main(String[] args) {
        String input1 = "LCLYTHIGRNIYYGSYLYSETWNTGIMLLLITMATAFMGYVLPWGQMSFWGATVITNLFSAIPYIGTNLV";
        String input2 = "EWIWGGFSVDKATLNRFFAFHFILPFTMVALAGVHLTFLHETGSNNPLGLTSDSDKIPFHPYYTIKDFLG";
        System.out.println(SDF.SDFfunc(input1,input2,100));

    }

}