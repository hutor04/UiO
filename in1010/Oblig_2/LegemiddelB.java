class LegemiddelB extends Legemiddel {

    // Properties

    private final int strength;

    // Constructor

    public LegemiddelB(String newName, double newPrice, double newSubstance, int newStrength) {
        super(newName, newPrice, newSubstance);
        this.strength = newStrength;
    }

    // Getter methods

    public int hentVanedannendeStyrke() {
        return this.strength;
    }

}
