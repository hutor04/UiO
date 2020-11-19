public class Lege implements Comparable<Lege> {

    // Properties

    private final String name;
    private Lenkeliste<Resept> recipeList = new Lenkeliste<Resept>();

    // Constructor

    public Lege(String newName) {
        this.name = newName;
    }

    // Getter methods

    public String getName() {
        return name;
    }

    public Lenkeliste<Resept> getRecipeList() {
        return recipeList;
    }

    // Setter Methods

    public void addRecipe(Resept newRecipe) {
        this.recipeList.leggTil(newRecipe);
    }

    @Override
    public int compareTo(Lege otherDoctor) {
        return name.compareTo(otherDoctor.getName());
    }

    @Override
    public String toString() {
        return String.format("DOCTOR Name: %s, No. of Recipes: %d\n", this.name, this.recipeList.stoerrelse());
    }
}
