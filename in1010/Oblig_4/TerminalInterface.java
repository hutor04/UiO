import java.util.Scanner;

public class TerminalInterface {
    MainProgram program = new MainProgram();

    // Main Menu
    private String MAIN_MENU = "0: Print out all data\n" +
            "1: Add data...\n" +
            "2: Use a recipe...\n" +
            "3: Show statistics...\n" +
            "4: Print data to file...\n" +
            "q: Quit program\n" +
            "Enter command: ";
    private String GET_TO_MAIN_MENU = "Enter 'q' to get back to main menu: ";


    // Add data
    private String ADD_DATA_MENU = "0: Load from file...\n" +
            "1: Add a doctor...\n" +
            "2: Add a patient...\n" +
            "3: Add a drug...\n" +
            "4: Add a recipe...\n" +
            "q: Back to main menu...";

    // Load from file
    private final String ENTER_FILE_NAME = "Enter file name, to load data from file or enter 'q' to quit to the main menu: ";
    private final String FILE_LOAD_SUCCESS = "Data loaded sucessfully. Going to the main menu.";
    private final String FILE_LOAD_FAIL = "Failed to load the data. Going to the main menu.";

    // Manual Load
    private String ADD_DOCTOR = "Input doctor's name and contract number (comma separated): ";
    private String ADD_PATIENT = "Input patient's name and national ID number (comma separated): ";
    private String ADD_DRUG = "Input drug's name, type, price, quantity, active substance [, strength] (comma separated): ";
    private String ADD_RECIPE = "Input recipe's type, drug ID, Doctor's name, Patient's ID, [No. of Uses] (comma separated): ";

    private String ADD_SUCCESS = "Success! Add another record y/n?: ";
    private String ADD_FAIL = "Failed to add a record. Check input format. Try again y/n?: ";
    private String RECIPE_FAIL = "Failed to add a record. Make sure that doctor, patient, drug exist in the system!" +
            "And Check input format. Try again y/n?: ";

    // Using recipe.
    private final String NO_PATIENTS = "There are no patients in the System.\n";
    private final String WRONG_INPUT = "Wrong input. Try again: ";
    private final String NO_RECIPES = "The patient has no recipes.\n";
    private String CHOOSE_PATIENT = "Choose a patient (or 'q' to get back): ";
    private String LIST_RECIPES = "Choose a recipe (or 'q' to get back): ";
    private final String USING_RECIPE = "Used recipe for %s. Uses left: %d\n";
    private final String RECIPE_STATUS = "%d: Drug: %s, Uses Left: %s";

    // Adding File
    private final String ADD_FILE = "Enter export file name or 'q' to get back to the main menu: ";
    private final String SUCCEFULL_SAVE = "We succefully saved the file. Going to main menu.\n";
    private final String FAILED_SAVE = "Failed to save the file. Going to the main menu.\n";

    // Menu Actions
    private final String BACK = "q";
    private final String OK = "y";
    private final String NO = "n";
    private final String ITEM_0 = "0";
    private final String ITEM_1 = "1";
    private final String ITEM_2 = "2";
    private final String ITEM_3 = "3";
    private final String ITEM_4 = "4";

    private void getBackMainMenu(Scanner userInput) {
        boolean ready = false;
        while (!ready) {
        System.out.print(GET_TO_MAIN_MENU);
        if (userInput.hasNext() && userInput.nextLine().equals(BACK)) {
            ready = true;
            this.mainMenu();
        }
        }

    }

    public void mainMenu() {
        System.out.println(MAIN_MENU);
        Scanner input = new Scanner(System.in);
        String command = "";

            if (input.hasNext()) {
                command = input.nextLine();
            }
            if (command.equals(BACK)) {
                System.exit(0);
            } else if (command.equals(ITEM_0)) {
                this.printDataToScreen();
                this.getBackMainMenu(input);
                }
              else if (command.equals(ITEM_1)) {
                this.loadDataLoop();
            } else if (command.equals(ITEM_2)) {
                this.useRecipe();
            } else if (command.equals(ITEM_3)) {
                this.showStatistics();
                this.getBackMainMenu(input);
            } else if (command.equals(ITEM_4)) {
                this.writeDataToFile();
            }




        }

    public void loadDataFromFile() {
        System.out.println(ENTER_FILE_NAME);
        String command = "";
        Scanner input = new Scanner(System.in);
        if (input.hasNext()) {
            command = input.nextLine();
        }
        if (command.equals(BACK)) {
            this.mainMenu();
        } else {
            boolean action = program.loadDataFile(command);
            if (action) {
                System.out.println(FILE_LOAD_SUCCESS);
                this.mainMenu();
            } else {
                System.out.println(FILE_LOAD_FAIL);
                this.mainMenu();
            }
        }

    }

    public void loadDataLoop() {
        System.out.println(ADD_DATA_MENU);
        Scanner input = new Scanner(System.in);
        String command = "";

        if (input.hasNext()) {
            command = input.nextLine();
        }

        if (command.equals(BACK)) {
            this.mainMenu();
        } else if (command.equals(ITEM_0)) {
            this.loadDataFromFile();
        } else if (command.equals(ITEM_1)) {
            this.addDoctor();
        } else if (command.equals(ITEM_2)) {
            this.addDPatient();
        } else if (command.equals(ITEM_3)) {
            this.addDrug();
        } else if (command.equals(ITEM_4)) {
            this.addRecipe();
        }
    }

    // Add New Doctor
    public void addDoctor() {
        System.out.println(ADD_DOCTOR);
        Scanner input = new Scanner(System.in);
        String command = "";

        if (input.hasNextLine()) {
            command = input.nextLine();
        }

        boolean ready = false;
        while(!ready) {
            if (program.addNewDoctor(command)) {
                System.out.println(ADD_SUCCESS);
                if (input.hasNextLine()) {
                    command = input.nextLine();
                }

                if (command.equals(OK)) {
                    ready = true;
                    this.addDoctor();
                } else if (command.equals(NO)) {
                    ready = true;
                    this.loadDataLoop();
                }
            } else {
                System.out.println(ADD_FAIL);
                if (input.hasNextLine()) {
                    command = input.nextLine();
                }

                if (command.equals(OK)) {
                    ready=true;
                    this.addDoctor();
                } else if (command.equals(NO)) {
                    ready=true;
                    this.loadDataLoop();
                }
            }
        }

    }

    // Add New Patient
    public void addDPatient() {
        System.out.println(ADD_PATIENT);
        Scanner input = new Scanner(System.in);
        String command = "";

        if (input.hasNextLine()) {
            command = input.nextLine();
        }

        boolean ready = false;
        while(!ready) {
            if (program.addNewPatient(command)) {
                System.out.println(ADD_SUCCESS);
                if (input.hasNextLine()) {
                    command = input.nextLine();
                }

                if (command.equals(OK)) {
                    ready = true;
                    this.addDPatient();
                } else if (command.equals(NO)) {
                    ready = true;
                    this.loadDataLoop();
                }
            } else {
                System.out.println(ADD_FAIL);
                if (input.hasNextLine()) {
                    command = input.nextLine();
                }

                if (command.equals(OK)) {
                    ready = true;
                    this.addDPatient();
                } else if (command.equals(NO)) {
                    ready = true;
                    this.loadDataLoop();
                }
            }
        }
    }

    // Add New Drug
    public void addDrug() {
        System.out.println(ADD_DRUG);
        Scanner input = new Scanner(System.in);
        String command = "";

        if (input.hasNextLine()) {
            command = input.nextLine();
        }

        boolean ready = false;
        while(!ready) {
            if (program.addNewDrug(command)) {
                System.out.println(ADD_SUCCESS);
                if (input.hasNextLine()) {
                    command = input.nextLine();
                }

                if (command.equals(OK)) {
                    ready = true;
                    this.addDrug();
                } else if (command.equals(NO)) {
                    this.loadDataLoop();
                }
            } else {
                System.out.println(ADD_FAIL);
                if (input.hasNextLine()) {
                    command = input.nextLine();
                }

                if (command.equals(OK)) {
                    ready = true;
                    this.addDrug();
                } else if (command.equals(NO)) {
                    ready = true;
                    this.loadDataLoop();
                }
            }
        }
    }

    // Add new recipe
    public void addRecipe() {
        System.out.println(ADD_RECIPE);
        Scanner input = new Scanner(System.in);
        String command = "";

        if (input.hasNextLine()) {
            command = input.nextLine();
        }

        boolean ready = false;
        while(!ready) {
            if (program.addNewRecipe(command)) {
                System.out.println(ADD_SUCCESS);
                if (input.hasNextLine()) {
                    command = input.nextLine();
                }

                if (command.equals(OK)) {
                    ready = true;
                    this.addRecipe();
                } else if (command.equals(NO)) {
                    ready = true;
                    this.loadDataLoop();
                }
            } else {
                System.out.println(RECIPE_FAIL);
                if (input.hasNextLine()) {
                    command = input.nextLine();
                }

                if (command.equals(OK)) {
                    ready = true;
                    this.addRecipe();
                } else if (command.equals(NO)) {
                    ready = true;
                    this.loadDataLoop();
                }
            }
        }
    }

    // Use Recipe
    public void useRecipe() {
        Scanner input = new Scanner(System.in);
        String action = "";
        Pasient choice = null;

        Lenkeliste<Pasient> patients = program.getPatientsList();
        if (patients.stoerrelse() == 0) {
            System.out.println(NO_PATIENTS);
            this.mainMenu();
        }

        int i = 0;
        for (Pasient patient: patients) {
            System.out.println(String.format("%d: Name: %s, ID: %s", i, patient.getName(), patient.getNationalID()));
            i++;
        }

        System.out.println(CHOOSE_PATIENT);



        boolean ready = false;
        while(!ready) {

            if (input.hasNextLine()) {
                action = input.nextLine();
            }

            if (action.equals(BACK)) {
                ready = true;
                this.mainMenu();
            } else if (action.matches("[0-9]+") && Integer.parseInt(action) >= 0 && Integer.parseInt(action) <
                    patients.stoerrelse()) {
                ready = true;
                choice = patients.hent(Integer.parseInt(action));

            }
        }

        System.out.println(LIST_RECIPES);

        i = 0;
        for (Resept recipe: choice.getRecipeList()) {
            System.out.println(String.format(RECIPE_STATUS, i, recipe.hentLegemiddel().hentNavn(),
                    recipe.hentReit()));
            i++;
        }

        ready = false;
        while(!ready) {
            if (input.hasNextLine()) {
                action = input.nextLine();
            }

            if (action.equals(BACK)) {
                ready = true;
                this.mainMenu();
            } else if (action.matches("[0-9]+") && Integer.parseInt(action) >= 0 && Integer.parseInt(action) <
                    choice.getRecipeList().stoerrelse() &&
                    choice.getRecipeList().hent(Integer.parseInt(action)).hentReit() > 0) {
                ready = true;
                Resept choiceRecipe = choice.getRecipeList().hent(Integer.parseInt(action));
                choiceRecipe.bruk();
                System.out.println(String.format(USING_RECIPE,
                        choiceRecipe.hentLegemiddel().hentNavn(), choiceRecipe.hentReit()));
                this.mainMenu();

            }
        }





    }

    // Displays the statistics
    public void showStatistics() {
        System.out.println(program.showStatistics());
    }

    // Displays all the data
    public void printDataToScreen() {
        System.out.println(program.getAllData());
    }

    // Write data to file
    public void writeDataToFile() {
        Scanner input = new Scanner(System.in);
        String command = "";
        boolean ready = false;

        System.out.println(ADD_FILE);
        while (!ready) {
            if (input.hasNextLine()) {
                command = input.nextLine();

                if (command.equals(BACK)) {
                    ready = true;
                    this.mainMenu();
                } else {
                    if (program.writeToFile(command)) {
                        ready = true;
                        System.out.println(SUCCEFULL_SAVE);
                        this.mainMenu();
                    } else {
                        ready = true;
                        System.out.println(FAILED_SAVE);
                    }
                }


            }
        }

    }

    // Main Interface loop
    public void mainLoop() {
        this.loadDataFromFile();
        this.mainMenu();
    }

    public static void main(String[] args) {
        TerminalInterface terminal = new TerminalInterface();
        terminal.mainLoop();
    }
}
