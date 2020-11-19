class ReseptHvite extends Resept {

    // Properties

    private static final String COLOUR = "hvit";

    // Constructor

    public ReseptHvite(Legemiddel newDrug, Lege newDoctor, Pasient newPatient, int reit) {
        super(newDrug, newDoctor, newPatient, reit);
    }

    // Getter Methods

    public String farge() {
        return COLOUR;
    }

    public double prisAaBetale() {
        return this.hentLegemiddel().hentPris();
    }

}
