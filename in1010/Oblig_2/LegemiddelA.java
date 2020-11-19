class LegemiddelA extends Legemiddel {

    // Properties

    private final int strength;

    // Constructor

    public LegemiddelA(String newName, double newPrice, double newSubstance, int newStrength) {
        super(newName, newPrice, newSubstance);
        this.strength = newStrength;
    }

    // Getter methods

    public int hentNarkotiskStyrke() {
        return this.strength;
    }

}
