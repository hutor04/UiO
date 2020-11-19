public class ReseptHviteMilitar extends ReseptHvite {

    // Properties

    private static final double DISCOUNT = 1.0;

    // Constructor

    public ReseptHviteMilitar(Legemiddel newDrug, Lege newDoctor, int newPatient, int reit) {
        super(newDrug, newDoctor, newPatient, reit);
    }

    // Getter Methods

    @Override
    public double prisAaBetale() {
        return this.hentLegemiddel().hentPris() - DISCOUNT * this.hentLegemiddel().hentPris();
    }
}
