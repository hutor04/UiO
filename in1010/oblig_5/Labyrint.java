import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Labyrint {
    // Misc
    private final static String EMPTY_FIELD_ICON = ".";
    private final static String WALL_FIELD_ICON = "#";
    ArrayList<String> res = new ArrayList<>();

    // Labyrinth Dimensions
    private int rows;
    private int cols;

    // Labyrinth Field
    public Rute[][] field;

    // Labyrinth Constructor
    private Labyrint(Rute[][] newField, int newRows, int newCols) {
        this.field = newField;
        this.rows = newRows;
        this.cols = newCols;
    }

    // Static Factory
    public static Labyrint lesFraFil(File newFile) throws FileNotFoundException {

        // Scanner object
        Scanner input = new Scanner(newFile);

        // Read dimensions
        String[] dimensions = input.nextLine().split(" ");
        int newRows = Integer.parseInt(dimensions[0]);
        int newCols = Integer.parseInt(dimensions[1]);


        // Create new field
        Rute[][] newField = new Rute[newRows][newCols];

        // Labyrinth object
        Labyrint newLabyrinth = new Labyrint(newField, newRows, newCols);

        // Populate the new field
        for (int row = 0; row < newRows; row++) {
            String str = input.nextLine();

            for (int col = 0; col < newCols; col++) {
                String curChar = Character.toString(str.charAt(col));

                // Detect openings
                if ((row == 0 || row == newRows - 1 || col == 0 || col == newCols - 1) && curChar.equals(EMPTY_FIELD_ICON)) {
                    newLabyrinth.field[row][col] = new Aapning(newLabyrinth, row, col);

                // Detect paths
                } else if (curChar.equals(EMPTY_FIELD_ICON)) {
                    newLabyrinth.field[row][col] = new HvitRute(newLabyrinth, row, col);

                // Detect walls
                } else if (curChar.equals(WALL_FIELD_ICON)) {
                    newLabyrinth.field[row][col] = new SortRute(newLabyrinth, row, col);
                }


            }
        }

        // Update neighrbours
        for (int row = 0; row < newRows; row++) {
            for (int col = 0; col < newCols; col++) {
                newField[row][col].updateNeighbours();
            }
        }
        /*
        for (int row = 0; row < newRows; row++) {
            for (int col = 0; col < newCols; col++) {
                newField[row][col].findExits();
            }
        }*/

        return newLabyrinth;
    }

    @Override
    public String toString() {
        // Add size
        String result = String.format("%d, %d\n", this.rows, this.cols);

        // Add cells
        for (int row = 0; row < this.rows; row++) {
            String r_string = "";
            for (int col = 0; col < this.cols; col++) {
                r_string += this.field[row][col].tilTegn();
            }
            result += r_string + "\n";
        }

        // Return result
        return result;
    }

    // Return cell
    public Rute getCell(int row, int col) {
        return this.field[row][col];
    }

    // Get number of rows
    public int getRows() {
        return this.rows;
    }

    // Get number of columns
    public int getColumns() {
        return this.cols;
    }

    // Find all exits
    public void finnUtvei() {
        Lenkeliste<Rute> q = new Lenkeliste<>();
        q.leggTil(this.field[0][0]);
        Lenkeliste<Rute> result = this.field[0][0].gaaBFS(q, new Lenkeliste<>());
        if (result.stoerrelse() == 0) {
            System.out.println("There are no exits.");
        } else {
            System.out.println("We found the following exits:");
            for (Rute cell: result) {System.out.println(cell);}
        }

    }

    // Find Exits from the defined cell
    public ArrayList<String> finnUtveiFra(int col, int row) {
        ArrayList<String> output = new ArrayList<>();
        HashSet<String> r = this.field[row][col].gaaDFS("", new Stack<>(), new HashSet<>(), new ArrayList<>());
        for (String s: r) {
            output.add(s);}
        return output;
    }



}

class TestMe {
    public static void main(String[] args) throws FileNotFoundException {
        File inFile = new File("/Users/yauhenkhutarniuk/Documents/UiO/in1010/oblig_5/labyrinth/6.in");
        Labyrint l_1 = Labyrint.lesFraFil(inFile);
        /*ArrayList<String> r2 = l_1.finnUtveiFra(10,11);
        System.out.println(r2.size());
        System.out.println(l_1.getCell(10, 11).getNeighbours()[3].isWall());
        //for (String s: r) {System.out.println(s);}*/

        l_1.getCell(1, 1).gaa();
        System.out.println(l_1.res.size());



    }}





