class ValidateObjects {
    public static Pasient validatePatient(Lenkeliste<Pasient> list, int id) {
        Pasient result = null;

        for (Pasient patient: list) {
            if (patient.getPatientID() == id) {
                result = patient;
            }
        }

        return result;
    }

    public static Legemiddel validateDrug(Lenkeliste<Legemiddel> list, int id) {
        Legemiddel result = null;

        for (Legemiddel drug: list) {
            if (drug.hentId() == id) {
                result = drug;
            }
        }

        return result;
    }

    public static Lege validateDoctor(SortertLenkeliste<Lege> list, String name) {
        Lege result = null;

        for (Lege doctor: list) {
            if (doctor.getName().equals(name)) {
                result = doctor;
            }
        }

        return result;
    }

}

