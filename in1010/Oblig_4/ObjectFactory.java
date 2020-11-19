public class ObjectFactory {
    private static final String A_DRUG = "a";
    private static final String B_DRUG = "b";
    private static final String C_DRUG = "c";
    private static final String BLUE_RECIPE = "blaa";
    private static final String WHITE_RECIPE = "hvit";
    private static final String PREVENTION_RECIPE = "prevensjon";
    private static final String MILITARY_RECIPE = "militaer";
    private static final String PATIENT_FILTER = "(?:[a-zA-Z]| |\\.)+, ?[0-9]{11}";
    private static final String DOCTOR_FILTER = "(?:[a-zA-Z]| |\\.)+, ?[0-9]+";
    private static final String DRUG_FILTER = "(?:[a-zA-Z]| |\\.)+, ?(?:[abcABC]), ?[0-9]+, ?[0-9]+(?:, ?[0-9]+)?";
    private static final String RECIPE_FILTER = "(?:blaa|hvit|prevensjon|militaer), ?[0-9]+, ?(?:[a-zA-Z]| |\\.)+, ?[0-9]+(?:, ?[0-9]+)?";

    // Reads String, returns Pasient object

    public static Pasient createPatient(String inputString) {
        String[] inputData;

        if (inputString == null || !inputString.matches(PATIENT_FILTER)) {
            return null;
        } else {
            inputData = inputString.split(", ");
            Pasient newPatient = new Pasient(inputData[0], inputData[1]);
            return newPatient;
        }

    }

    // Reads string returns Legemiddel object

    public static Legemiddel createDrug(String inputString) {
        String[] inputData;
        if (inputString == null ||
                !inputString.matches(DRUG_FILTER)) {
            return null;
        } else {

            inputData = inputString.split(", ");

            if (inputData[1].toLowerCase().equals(C_DRUG)) {
                return new LegemiddelC(inputData[0], Double.parseDouble(inputData[2]), Double.parseDouble(inputData[3]));

            } else if (inputData[1].toLowerCase().equals(A_DRUG)) {
                return new LegemiddelA(inputData[0], Double.parseDouble(inputData[2]), Double.parseDouble(inputData[3]),
                        Integer.parseInt(inputData[4]));

            } else if (inputData[1].toLowerCase().equals(B_DRUG)) {
                return new LegemiddelB(inputData[0], Double.parseDouble(inputData[2]), Double.parseDouble(inputData[3]),
                        Integer.parseInt(inputData[4]));

            }  else {
                return null;
            }
        }
    }

    // Reads a string, returns Lege object

    public static Lege createDoctor(String inputString) {
        String[] inputData;
        if (inputString == null || !inputString.matches(DOCTOR_FILTER)) {
            return null;
        } else {
            inputData = inputString.split(", ");
            if (Integer.parseInt(inputData[1]) == 0) {
                return new Lege(inputData[0]);
            } else {
                return new Fastlege(inputData[0], Integer.parseInt(inputData[1]));
            }
        }

    }

    // Reads a string, returns Resept object

    public static Resept createRecipe(Lenkeliste<Pasient> patientList, Lenkeliste<Legemiddel> drugsList,
                                      SortertLenkeliste<Lege> doctorsList, String inputString) {
        String[] inputData;
        Pasient patient;
        Legemiddel drug;
        Lege doctor;

        if (inputString == null ||
                !inputString.matches(RECIPE_FILTER)) {
            return null;
        } else {
            inputData = inputString.split(", ");


        }

        patient = ValidateObjects.validatePatient(patientList, Integer.parseInt(inputData[3]));
        drug = ValidateObjects.validateDrug(drugsList, Integer.parseInt(inputData[1]));
        doctor = ValidateObjects.validateDoctor(doctorsList, inputData[2]);

        if (drug == null || doctor == null || patient == null) {
            return null;
        } else {
            //  Resepter (type, legemiddelNummer, legeNavn, persID, [reit])
            Resept newRecipe = null;

            if (inputData[0].toLowerCase().equals(BLUE_RECIPE)) {
                newRecipe = new ReseptBlaa(drug, doctor, patient, Integer.parseInt(inputData[4]));

            } else if (inputData[0].toLowerCase().equals(WHITE_RECIPE)) {
                newRecipe = new ReseptHvite(drug, doctor, patient, Integer.parseInt(inputData[4]));

            } else if (inputData[0].toLowerCase().equals(PREVENTION_RECIPE)) {
                newRecipe = new ReseptHviteP(drug, doctor, patient);

            } else if (inputData[0].toLowerCase().equals(MILITARY_RECIPE)) {
                newRecipe = new ReseptHviteMilitar(drug, doctor, patient, Integer.parseInt(inputData[4]));


            }

            if (newRecipe != null) {
                doctor.addRecipe(newRecipe);
                patient.addRecipe(newRecipe);
            }

            return newRecipe;


        }
    }

}
