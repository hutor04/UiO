import java.util.ArrayList;
import java.util.HashSet;
import java.util.Stack;
import java.util.Random;


public abstract class Rute {

    // Cell Coordinates
    private int row;
    private int col;

    // Labyrinth that hosts the cell
    private Labyrint hostLabyrinth;

    // Neighbours N S W E
    private Rute[] neightbours = {null, null, null, null};

    // Incoming caller N S W E
    private Integer[] incomingCaller = {0, 0, 0, 0};

    private Integer[] incomingCallerMask = {1, 0, 3, 2};

    private ArrayList<String> solutions;


    // Constructor
    public Rute(Labyrint newHost, int newRow, int newCol) {
        this.hostLabyrinth = newHost;
        this.row = newRow;
        this.col = newCol;
        this.solutions = new ArrayList<>();
    }

    // Update neighbours
    public void updateNeighbours() {
        if (this.row - 1 >= 0) {
            this.neightbours[0] = this.hostLabyrinth.getCell(this.row - 1, this.col);
        }

        if (this.row + 1 < this.hostLabyrinth.getRows()) {
            this.neightbours[1] = this.hostLabyrinth.getCell(this.row + 1,this.col);
        }

        if (this.col - 1 >= 0) {
            this.neightbours[2] = this.hostLabyrinth.getCell(this.row,this.col - 1);
        }

        if (this.col + 1 < this.hostLabyrinth.getColumns()) {
            this.neightbours[3] = this.hostLabyrinth.getCell(this.row,this.col + 1);
        }

    }

    public Rute[] getNeighbours() {
        return this.neightbours;
    }

    public void findExits() {
        if (solutions.size() == 0) {
            HashSet<String> r = this.gaaDFS("", new Stack<>(), new HashSet<>(), new ArrayList<>());
            for (String s: r) {
                solutions.add(s);}
        }

    }

    public ArrayList<String> getSolutions() {
        return solutions;
    }

    // Cell status passable or not
    abstract boolean isWall();

    // Cell status exit or not
    abstract boolean isExit();

    // Representation of the cell
    abstract String tilTegn();

    public int getCol() {
        return this.col;
    }

    public int getRow() {
        return this.row;
    }

    @Override
    public String toString() {
        return String.format("%d,%d", this.row, this.col);
    }

    // Sets the direction of the incoming call
    public void setIncomingCaller(int fromDirection) {
        this.incomingCaller[fromDirection] = 1;
    }

    // Resets the incomingCaller array
    public void resetIncomingCaller() {
        for (int i = 0; i < this.incomingCaller.length; i++) {
            this.incomingCaller[i] = 0;
        }
    }

    //Find way-out from the labyrinth
    public String gaa() {

        //Current exit path
        String exitPath = "";
        exitPath += String.format("%s->", this.toString());

        // Check if this is exit
        if (this.isExit()) {
            exitPath = exitPath.substring(0, exitPath.length() - 2);
            hostLabyrinth.res.add(exitPath);
            return exitPath;
        }

        // Check the dead end and set up available routes
        boolean deadEnd = true;
        Rute[] availableRoutes = new Rute[4]; // These are available routes
        for (int i = 0; i < this.neightbours.length; i++) {
            if (this.neightbours[i] != null && !this.neightbours[i].isWall() && this.incomingCaller[i] != 1) {
                availableRoutes[i] = this.neightbours[i];
                deadEnd = false;
            }
        }

        if (deadEnd) {
            return null;
        }

        // Explore other options
        String[] otherOptions = {null, null, null, null};
        for (int i = 0; i < availableRoutes.length; i++) {
            if (availableRoutes[i] != null) {
                // Set incoming caller for the next cell
                if (i == 0) {
                    this.neightbours[i].setIncomingCaller(1);
                } else if (i == 1) {
                    this.neightbours[i].setIncomingCaller(0);
                } else if (i == 2) {
                    this.neightbours[i].setIncomingCaller(3);
                } else if (i == 3) {
                    this.neightbours[i].setIncomingCaller(2);
                }
                // Result from other branches
                String nextOptions = availableRoutes[i].gaa();
                if (nextOptions != null) {
                    otherOptions[i] = nextOptions;
                }

            }
        }

        // If other branches failed, return null or return the exits
        boolean noResults = true;
        for (String s : otherOptions) {
            if (s != null) {
                noResults = false;
                exitPath += s;
            }
        }

        return noResults ? null : exitPath;

    }

    //Find all from the labyrinth using breadth-first search
    public Lenkeliste<Rute> gaaBFS(Lenkeliste<Rute> queue, Lenkeliste<Rute> exits) {

        // Exit condition
        if (queue.stoerrelse() == 0) {
            return exits;
        }
        queue.fjern();

        // Check if this is exit
        if (this.isExit()) {
            exits.leggTil(this);
        }

        // Check the dead end and set up available routes
        for (int i = 0; i < this.neightbours.length; i++) {
            if (this.neightbours[i] != null && !this.neightbours[i].isWall() && this.incomingCaller[i] != 1) {
                this.neightbours[i].setIncomingCaller(incomingCallerMask[i]);
                queue.leggTil(this.neightbours[i]);
            }
        }

        if (queue.stoerrelse() != 0) {
            Rute nextCell = queue.hent(0);
            nextCell.gaaBFS(queue, exits);
        }

        return exits;
    }

    //Find all from the labyrinth using breadth-first search
    public HashSet<String> gaaDFS(String path, Stack<Rute> stack, HashSet<String> exitPaths,
                                  ArrayList<Rute> visitedCells) {

        String pathN = path;
        ArrayList<Rute> visitedN = (ArrayList<Rute>) visitedCells.clone();
        Stack<Rute> stackN = (Stack<Rute>) stack.clone();

        // Add the cell to visited cells list and add it to the current path
        visitedCells.add(this);
        //visitedN.add(this);
        pathN += String.format("%s->", this.toString());

        // Check if this is exit
        if (this.isExit()) {
            pathN = pathN.substring(0, pathN.length()-2);
            exitPaths.add(pathN);
            //System.out.println(pathN);
            //System.out.println(exitPaths.size());
            return exitPaths;
        }

        if (exitPaths.size() > 10) {return exitPaths;}

        // Find available next steps
        ArrayList<Rute> nextSteps = new ArrayList<>();
        for (int i = 0; i < this.neightbours.length; i++) {
            if (this.neightbours[i] != null && !this.neightbours[i].isWall() && !visitedCells.contains(this.neightbours[i]) &&
                    this.incomingCaller[i] != 1) {
                this.neightbours[i].setIncomingCaller(incomingCallerMask[i]);
                nextSteps.add(this.neightbours[i]);
            }
        }

        //if(nextSteps.size() == 0) {return exitPaths;}

        // If there are available steps add current cell to the stack
        if (nextSteps.size() > 0) {
            stackN.push(this);

            // Explore available steps
            for (Rute cell: nextSteps) {
                String clone_path = pathN;
                ArrayList<Rute> clone_visited = (ArrayList<Rute>) visitedN.clone();
                Stack<Rute> clone_stack = (Stack<Rute>) stackN.clone();
                cell.gaaDFS(clone_path, clone_stack, exitPaths, visitedCells);}
        }



        // If there are no available further steps, step back
        if (nextSteps.size() == 0 && !stackN.empty()) {
            Rute c = stackN.pop();
            String clone_path = pathN;
            ArrayList<Rute> clone_visited = (ArrayList<Rute>) visitedCells.clone();
            Stack<Rute> clone_stack = (Stack<Rute>) stackN.clone();
            c.gaaDFS(clone_path, clone_stack, exitPaths, clone_visited);

        }

        return exitPaths;}


    }
