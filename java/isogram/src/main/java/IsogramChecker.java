import java.util.*;

class IsogramChecker {

    boolean isIsogram(String phrase) {
        
        Set<Character> letters = new HashSet<>();
        phrase = phrase.replaceAll("[^a-zA-Z]", "").toLowerCase();
        
        for(char c : phrase.toCharArray()){
            letters.add(c);
        }
        return letters.size() == phrase.length();
    }
}
