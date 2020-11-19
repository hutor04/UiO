public class SortRute extends Rute {
    // Misc
    private String ICON = "#";

    // Constructor
    public SortRute(Labyrint newHost, int newRow, int newCol) {
        super(newHost, newRow, newCol);
    }

    // Cell status passable or not
    public boolean isWall() {
        return true;
    }

    // Cell status exit or not
    public boolean isExit() {
        return false;
    }

    // Representation of the cell
    public String tilTegn() {
        return ICON;
    }
}
