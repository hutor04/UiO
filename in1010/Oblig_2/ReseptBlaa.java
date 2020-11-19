public class ReseptBlaa extends Resept {

    // Properties

    private static final String COLOUR = "blaa";
    private static final double DISCOUNT = 0.75;

    // Constructor

    public ReseptBlaa(Legemiddel newDrug, Lege newDoctor, int newPatient, int reit) {
        super(newDrug, newDoctor, newPatient, reit);
    }

    // Getter Methods

    public String farge() {
        return COLOUR;
    }

    public double prisAaBetale() {
        return this.hentLegemiddel().hentPris() - DISCOUNT * this.hentLegemiddel().hentPris();
    }
}
