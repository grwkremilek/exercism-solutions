import java.util.List;

class ProteinTranslator {
    
    List<String> translate(String rnaSequence) {

    }
    
    
    private static String RnaTranslator(String subsequence) {
    switch(subsequence) {
        case "AUG": return "Methionine";
        case "UUU":
        case "UUC": return "Phenylalanine";
        case "UUA":
        case "UUA": return "Leucine";
        case "UCU":
        case "UCC":
        case "UCA":
        case "UCG": return "Serine";
        case "UGU":
        case "UGC": return "Cesteine";
        case "UGG": return "Tryptophan";
        case "UAA":
        case "UAG":
        case "UGA": return "STOP";
    }
}
