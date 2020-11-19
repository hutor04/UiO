public class ReseptHviteP extends ReseptHvite {

    // Properties

    private static final double DISCOUNT = 116.0;
    private static final int REIT = 3;

    // Constructor

    public ReseptHviteP(Legemiddel newDrug, Lege newDoctor, int newPatient, int reit) {
        super(newDrug, newDoctor, newPatient, REIT);
    }

    // Getter Methods

    @Override
    public double prisAaBetale() {
        double discountedPrice = this.hentLegemiddel().hentPris() - DISCOUNT;
        if (discountedPrice > 0) {
            return discountedPrice;
        } else {
            return 0;
        }
    }
}
