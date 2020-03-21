class Scrabble {
    
    private String word;
    private static final int[] LETTER_SCORES = {
            1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
            1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    Scrabble(String word) {
        this.word = word.toLowerCase();
    }

    int getScore() {
        int score = 0;
        for (char c : this.word.toCharArray()) {
            score += getLetterScore(c);
            }
        return score;
    }
    
    private int getLetterScore(char letter){
        return LETTER_SCORES[(int) letter - (int) 'a'];
        }
}
