import com.sun.tools.javac.Main;

import java.io.UnsupportedEncodingException;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

class MainProgram {
    // Object containers
    private Lenkeliste<Pasient> patientsList = new Lenkeliste<>();
    private Lenkeliste<Legemiddel> drugsList = new Lenkeliste<>();
    private SortertLenkeliste<Lege> doctorsList = new SortertLenkeliste<>();
    private Lenkeliste<Resept> recipeList = new Lenkeliste<>();

    // TEXT DATA
    // Beacons
    private final String BEACON = "#";
    private final String PATIENT_START = "# Pasienter";
    private final String DRUGS_START = "# Legemidler";
    private final String DOCTORS_START = "# Leger";
    private final String RECIPES_START = "# Resepter";

    // Drug types
    private final String A_DRUG = "a";
    private final String B_DRUG = "b";
    private final String C_DRUG = "c";

    // Recipe types
    private final String BLUE_RECIPE = "blaa";
    private final String WHITE_RECIPE = "hvit";
    private final String PREVENTION_RECIPE = "prevensjon";
    private final String MILITARY_RECIPE = "militaer";

    // Output Headers
    private final String PATIENT_HEADER = "# Pasienter (navn, fnr)";
    private final String DRUGS_HEADER = "# Legemidler (navn, type, pris, antall/mengde, virkestoff [, styrke])";
    private final String DOCTORS_HEADER = "# Leger (navn, avtalenr / 0 hvis ingen avtale)";
    private final String RECIPES_HEADER = "# Resepter (type, legemiddelNummer, legeNavn, persID, [reit])";

    // Misc
    private final String DUMMY_CONTRACT = "0";

    // MAIN FUNCTIONALITY

    // Print out the data
    public String getAllData() {
        String data = "";
        data += DRUGS_START + "\n";
        for (Legemiddel drug: drugsList) {
            data += drug.toString();
        }
        data += "\n";

        data += PATIENT_START + "\n";
        for (Pasient patient: patientsList) {
            data += patient.toString();
        }
        data += "\n";

        data += DOCTORS_START + "\n";
        for (Lege doctor: doctorsList) {
            data += doctor.toString();
        }
        data += "\n";

        data += RECIPES_START + "\n";
        for (Resept recipe:recipeList) {
            data += recipe.toString();
        }

        return data;
    }

    // Statistics
    public String showStatistics() {
        int quantityRecipesB_drug = 0;
        int quantityM_RecipesB_drug = 0;
        String doctorA_recipes = "";
        String patientsA_recipes = "";

        for (Resept recipe: recipeList) {
            if (recipe.hentLegemiddel() instanceof LegemiddelB) {
                quantityRecipesB_drug += 1;
            }

            if ((recipe.hentLegemiddel() instanceof LegemiddelB) && recipe instanceof ReseptHviteMilitar) {
                quantityM_RecipesB_drug += 1;
            }
        }

        for (Lege doctor: doctorsList) {
            int numberRecipes = 0;
            String doctorName = doctor.getName();
            for (Resept recipe: doctor.getRecipeList()) {
                if (recipe.hentLegemiddel() instanceof LegemiddelA) {
                    numberRecipes++;
                }
            }
            if (numberRecipes > 0) {
                doctorA_recipes += String.format("Name: %s, No. of Recipes: %d.\n", doctorName,
                        numberRecipes);
            }
        }

        for (Pasient patient: patientsList) {
            int numerRecipes = 0;
            String patientName = patient.getName();
            for (Resept recipe: patient.getRecipeList()) {
                if ((recipe.hentLegemiddel() instanceof  LegemiddelA) && recipe.hentReit() > 0) {
                    numerRecipes++;
                }
            }
            if (numerRecipes > 0) {
                patientsA_recipes += String.format("Name: %s, No. of Recipes: %d.\n",
                        patientName, numerRecipes);
            }
        }

        String result = String.format("Printing out statistiscs...\nTotal number of recipes with Type-B drug: %d\n" +
                        "\nTotal number of Military recipes with  Type-B drug: %d\n" +
                        "\nDoctors that prescribed Type-A drugs:\n%s" +
                        "\nPatients holding active recipes for Type-A drugs:\n%s",
                quantityRecipesB_drug, quantityM_RecipesB_drug, doctorA_recipes, patientsA_recipes);

        return result;



    }


    // Save data to file
    public boolean writeToFile(String fileName) {
        PrintWriter output;
        String outputData = "";

        outputData += PATIENT_HEADER + "\n";
        for (Pasient patient: patientsList) {
            outputData += patient.getName() + ", " + patient.getNationalID() + "\n";
        }

        outputData += DRUGS_HEADER + "\n";
        for (Legemiddel drug: drugsList) {
            if (drug instanceof LegemiddelA) {
                outputData += drug.hentNavn() + ", " + A_DRUG + ", " + (int) drug.hentPris() + ", " +
                        (int) drug.hentVirkestoff() + ", " + ((LegemiddelA) drug).hentNarkotiskStyrke() + "\n";
            } else if (drug instanceof LegemiddelB) {
                outputData += drug.hentNavn() + ", " + B_DRUG + ", " + (int) drug.hentPris() + ", " +
                        (int) drug.hentVirkestoff() + ", " + ((LegemiddelB) drug).hentVanedannendeStyrke() + "\n";
            } else {
                outputData += drug.hentNavn() + ", " + C_DRUG + ", " + (int) drug.hentPris() + ", " +
                        (int) drug.hentVirkestoff() + "\n";
            }
        }


        outputData += DOCTORS_HEADER + "\n";
        for (Lege doctor: doctorsList) {
            if (doctor instanceof Fastlege) {
                outputData += doctor.getName() + ", " + ((Fastlege) doctor).hentAvtalenummer() + "\n";
            } else {
                outputData += doctor.getName() + ", " + DUMMY_CONTRACT + "\n";
            }

        }

        outputData += RECIPES_HEADER + "\n";
        for (Resept recipe: recipeList) {
            String type = "";
            if (recipe instanceof ReseptBlaa) {
                type = BLUE_RECIPE;
            } else if (recipe instanceof ReseptHviteP) {
                type = PREVENTION_RECIPE;
            } else if (recipe instanceof ReseptHviteMilitar) {
                type = MILITARY_RECIPE;
            } else {
                type = PREVENTION_RECIPE;
            }
            outputData += type + ", " + recipe.hentLegemiddel().hentId() + ", " + recipe.hentLege().getName() +
                    ", " + recipe.hentPasientId().getPatientID() + ", " + recipe.hentReit() + "\n";
        }

        //System.out.println(outputData);

        try {
            output = new PrintWriter(fileName, "UTF-8");
            output.print(outputData);
            output.close();
            return true;
        } catch (FileNotFoundException | UnsupportedEncodingException e) {
            return false;
        }



    }


    // Load Data from File

    public boolean loadDataFile(String fileName) {
        File inputFile;
        Scanner input;

        try {
            inputFile = new File(fileName);
            input = new Scanner(inputFile);
            String currentLine = input.nextLine();
            while (input.hasNextLine()) {
                if (currentLine.startsWith(PATIENT_START) && input.hasNextLine()) {
                    currentLine = input.nextLine();
                    while (!currentLine.startsWith(BEACON)) {
                        addNewPatient(currentLine);
                        if (input.hasNextLine()) {currentLine = input.nextLine();} else {break;}
                    }
                }

                if (currentLine.startsWith(DRUGS_START) && input.hasNextLine()) {
                    currentLine = input.nextLine();
                    while (!currentLine.startsWith(BEACON)) {
                        addNewDrug(currentLine);
                        if (input.hasNextLine()) {currentLine = input.nextLine();} else {break;}
                    }
                }

                if (currentLine.startsWith(DOCTORS_START) && input.hasNextLine()) {
                    currentLine = input.nextLine();
                    while (!currentLine.startsWith(BEACON)) {
                        addNewDoctor(currentLine);
                        if (input.hasNextLine()) {currentLine = input.nextLine();} else {break;}
                    }
                }

                if (currentLine.startsWith(RECIPES_START) && input.hasNextLine()) {
                    currentLine = input.nextLine();
                    while (!currentLine.startsWith(BEACON)) {
                        addNewRecipe(currentLine);
                        if (input.hasNextLine()) {currentLine = input.nextLine();} else {break;}
                    }
                }

            }

        } catch (FileNotFoundException e) {
            return false;
        }

        return true;
    }



    public boolean addNewPatient(String newPatientData) {
        Pasient newPatient = ObjectFactory.createPatient(newPatientData);

        if (newPatient == null) {
            return false;

        } else {
            this.patientsList.leggTil(newPatient);
            return true;
        }
    }

    public boolean addNewDrug(String newDrugData) {
        Legemiddel newDrug = ObjectFactory.createDrug(newDrugData);

        if (newDrug == null) {
            return false;
        } else {
            this.drugsList.leggTil(newDrug);
            return true;
        }
    }

    public boolean addNewDoctor(String newDoctorData) {
        Lege newDoctor = ObjectFactory.createDoctor(newDoctorData);

        if (newDoctor == null) {
            return false;
        } else {
            this.doctorsList.leggTil(newDoctor);
            return true;
        }
    }

    public boolean addNewRecipe(String newDoctorData) {
        Resept newRecipe = ObjectFactory.createRecipe(patientsList, drugsList, doctorsList, newDoctorData);

        if (newRecipe == null) {
            return false;
        } else {
            this.recipeList.leggTil(newRecipe);
            return true;
        }
    }

    // Return patient names
    public Lenkeliste<Pasient> getPatientsList() {
        return patientsList;
    }

    public static void main(String[] args) {
        MainProgram p = new MainProgram();
        p.addNewPatient("AAA, 11111111111");
        p.addNewPatient("BBB, 11111111111");
        for (Pasient patient: p.patientsList) {
            System.out.println(patient);
        }
    }

}
