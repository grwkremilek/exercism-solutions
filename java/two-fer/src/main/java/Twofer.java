class Twofer {
    
    String twofer(String name) {
        String nameToDisplay = name == null ? "you" : name;
        return String.format("One for %s, one for me.", nameToDisplay);
    }
}
