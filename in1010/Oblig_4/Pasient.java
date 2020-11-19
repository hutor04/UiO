class Pasient {
    private static int idCounter = 0;

    private String name;
    private final String nationalID;
    private final int patientID;
    private Stabel<Resept> recipeList = new Stabel<>();

    public Pasient(String newName, String newNationalID) {
        this.patientID = idCounter;
        idCounter++;
        this.name = newName;
        this.nationalID = newNationalID;
    }

    //Getter Methods
    public String getName() {
        return name;
    }

    public String getNationalID() {
        return nationalID;
    }

    public int getPatientID() {
        return patientID;
    }

    public Stabel<Resept> getRecipeList() {
        return recipeList;
    }

    //Setter Methods
    public void addRecipe(Resept newRecipe) {
        recipeList.leggPaa(newRecipe);
    }

    @Override
    public String toString() {
        return String.format("PATIENT Patient ID: %d, Name: %s, National ID: %s, Assigned Recipes: %d\n", this.patientID,
                this.name, this.nationalID, this.recipeList.stoerrelse());
    }
}




