import java.util.*;

class Acronym {
    
    private String phrase;

    Acronym(String phrase) {
        this.phrase = phrase.replaceAll(" +", " ").replace("-", " ").replace("'", "").replaceAll("( )+", " ");
    }

    String getAcronym() {
        List<String> letters = new ArrayList<String>();
        String firstLetter  = "";
        
        String[] words = this.phrase.split(" ");
        
        for ( String word : words) {
            firstLetter = word.substring(0, 1).toUpperCase( );
            letters.add(firstLetter);
        }
        
        return String.join("", letters);
    }
}
