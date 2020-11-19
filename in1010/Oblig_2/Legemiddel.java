class Legemiddel {

    // Properties

    private static int idCounter = 0;
    private final int id;
    private final String name;
    private final double activeSubstance;
    private double price;

    // Constructor

    public Legemiddel(String newName, double newPrice, double newSubstance) {
        this.id = idCounter;
        idCounter++;
        this.name = newName;
        this.price = newPrice;
        this.activeSubstance = newSubstance;
    }

    // Getter methods

    public int hentId() {
        return this.id;
    }

    public String hentNavn() {
        return this.name;
    }

    public double hentPris() {
        return this.price;
    }

    public double hentVirkestoff() {
        return this.activeSubstance;
    }

    //  Setter methods

    public void settNyPris(double newPrice) {
        this.price = newPrice;
    }

}
