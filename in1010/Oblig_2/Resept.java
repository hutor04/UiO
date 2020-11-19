abstract class Resept {

    // Properties

    private static int idCounter = 0;
    private final int id;
    private final Legemiddel drug;
    private final Lege doctor;
    private final int patientID;
    private int reit;

    // Constructor

    public Resept(Legemiddel newDrug, Lege newDoctor, int newPatient, int reit) {
        this.id = idCounter;
        idCounter++;
        this.drug = newDrug;
        this.doctor = newDoctor;
        this.patientID = newPatient;
        this.reit = reit;
    }

    // Getter methods

    public int hentId(){
        return this.id;
    }

    public Legemiddel hentLegemiddel() {
        return this.drug;
    }

    public Lege hentLege() {
        return this.doctor;
    }

    public int hentPasientId() {
        return this.patientID;
    }

    public int hentReit() {
        return this.reit;
    }

    // Mutator methods

    public boolean bruk() {
        if (this.reit > 0) {
            reit--;
            return true;
        } else {
            return false;
        }
    }

    // Abstract methods

    public abstract String farge();

    public abstract double prisAaBetale();


}
