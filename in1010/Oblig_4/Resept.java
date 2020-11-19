abstract class Resept {

    // Properties

    private static int idCounter = 0;
    private final int id;
    private final Legemiddel drug;
    private final Lege doctor;
    private final Pasient patientID;
    private int reit;

    // Constructor

    public Resept(Legemiddel newDrug, Lege newDoctor, Pasient newPatient, int reit) {
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

    public Pasient hentPasientId() {
        return this.patientID;
    }

    public int hentReit() {
        return this.reit;
    }

    // Setter methods

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

    @Override
    public String toString() {
        return String.format("RECIPE ID: %d, Drug Name: %s, Doctor's Name: %s, Patients ID: %d, Uses Left: %d\n",
                this.id, this.drug.hentNavn(), this.doctor.getName(), this.patientID.getPatientID(), this.reit);
    }


}
