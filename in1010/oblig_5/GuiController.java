import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Color;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;

class GuiController {
    private Stage stage;
    private MazeView view;
    private Labyrint maze;
    private ArrayList<myRectangle> cells = new ArrayList<>();
    private Rute selectedCell;
    private File mazeFile;
    String path;
    private ArrayList<String> results = new ArrayList<>();
    private int pointer = 0;

    public GuiController(Stage stage, MazeView view) {
        this.stage = stage;
        this.view = view;
        this.mazeFile = new File("/Users/yauhenkhutarniuk/Documents/UiO/in1010/oblig_5/labyrinth/6.in");
        this.path = this.mazeFile.getAbsolutePath();
        try {
            this.maze = Labyrint.lesFraFil(this.mazeFile);
        } catch (FileNotFoundException e) {}
        this.drawMaze();

        this.view.getLoadButton().setOnAction(new ChooseFile());
        this.view.getFindExit().setOnAction(new ExitFinder());
        this.view.getNextResult().setOnAction(new showNextSolution());
        this.view.getPrevResult().setOnAction(new showPrevSolution());
        this.view.getResetView().setOnAction(new resetView());

    }

    // Populates the grid with the cells
    public void drawMaze() {
        // Building the field
        for (int i = 0; i < this.maze.field.length; i++) {
            for (int j = 0; j < this.maze.field[i].length; j++) {
                myRectangle field = new myRectangle(10, 10, this.maze.field[i][j]);
                if (!this.maze.field[i][j].isWall()) {
                    field.setOnMouseClicked(new SelectCell(field));
                }
                view.getGrid().add(field, j, i);
                this.cells.add(field);

            }
        }

    }

    // Shows route from the selected cell
    public void drawPath() {
        cells.forEach(myRectangle::deSelect);
        view.getInAppTitle().setText(String.format("Showing exit: %d out of %d", pointer + 1, results.size()));
        String[] route = results.get(pointer).split("->");
        for (String s : route) {
            String[] coordinates = s.split(",");
            int row = Integer.parseInt(coordinates[0]);
            int col = Integer.parseInt(coordinates[1]);
            myRectangle cell = (myRectangle) view.getGrid().getChildren().get(row * maze.getColumns() + col);
            cell.setFill(Color.RED);
        }
    }

    // Select Cell
    class SelectCell implements EventHandler<MouseEvent> {
        myRectangle f;
        public SelectCell(myRectangle field) {
            f = field;
        }
        @Override
        public void handle(MouseEvent event) {
            cells.forEach(myRectangle::deSelect);
            f.setFill(Color.RED);
            f.select();
            f.getCell().findExits();
            selectedCell = f.getCell();
            view.getInAppTitle().setText(String.format("Selected Row: %d, Col %d", selectedCell.getRow(), selectedCell.getCol()));
        }
    }


    // Find exit
    class ExitFinder implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
            pointer = 0;
            if (selectedCell != null) {
                results = selectedCell.getSolutions();
                view.getInAppTitle().setText(String.format("Found exits: %d", results.size()));
                if (results.size() > 0) {
                    drawPath();
                }

            } else {
                view.getInAppTitle().setText("Select a cell first!!");
            }
        }
    }

    // Show next solution
    class showNextSolution implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
            if (results.size() > 0 && results != null) {
                if (pointer < results.size()-1) {
                    pointer++;
                }
                drawPath();

            } else {
                view.getInAppTitle().setText("No results to display!");
            }
        }
    }

    // Show Previous Solution
    class showPrevSolution implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
            if (results.size() > 0 && results != null) {
                if (pointer > 0) {
                    pointer--;
                }
                drawPath();

            } else {
                view.getInAppTitle().setText("No results to display!");
            }
        }
    }

    // Reset view
    class resetView implements EventHandler<ActionEvent> {
        @Override
        public void handle(ActionEvent event) {
            cells.forEach(myRectangle::deSelect);
            view.getInAppTitle().setText("Maze Walker");
            selectedCell = null;
            results = null;
            view.getGrid().getChildren().clear();
            try {
                mazeFile = new File(path);
                maze = Labyrint.lesFraFil(mazeFile);
            } catch (FileNotFoundException e) {}
            drawMaze();
        }
    }

    // File Opener
    class ChooseFile implements EventHandler<ActionEvent> {

        @Override
        public void handle(ActionEvent event) {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setInitialDirectory(new File("."));
            fileChooser.setTitle("Select Maze File");
            fileChooser.getExtensionFilters().addAll(
            new FileChooser.ExtensionFilter("Maze Files", "*.in"));
            mazeFile = fileChooser.showOpenDialog(stage);
            if (mazeFile == null) {
                return;
            }
            try {
                path = mazeFile.getAbsolutePath();
                maze = Labyrint.lesFraFil(mazeFile);
            } catch (FileNotFoundException e) {
                System.out.println("File not found");
            }
            view.getGrid().getChildren().clear();
            drawMaze();

        }
    }

}
