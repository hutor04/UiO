import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.layout.HBox;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;


public class MazeView {
    private Stage stage;
    private BorderPane root;
    private Text inAppTitle;
    private GridPane grid;
    private Button loadButton;
    private Button findExit;
    private Button prevResult;
    private Button nextResult;
    private Button resetView;

    public MazeView(Stage newStage) {
        this.stage = newStage;
        this.root = new BorderPane();
        this.root.autosize();
        buildView();
    }

    // Return title
    public Text getInAppTitle() {
        return inAppTitle;
    }

    // Return load button
    public Button getLoadButton() {
        return this.loadButton;
    }

    // Return Find Exit button
    public Button getFindExit() {
        return findExit;
    }

    // Return previous result button
    public Button getPrevResult() {
        return prevResult;
    }

    // Return next result button
    public Button getNextResult() {
        return nextResult;
    }

    // Return reset button
    public Button getResetView() {
        return resetView;
    }

    // Return Grid pane
    public GridPane getGrid() {
        return this.grid;
    }

    void buildView() {
        // Create grid object
        this.grid = new GridPane();

        // Buttons
        this.loadButton = new Button("Load Maze");
        this.findExit = new Button("Find Exit");
        this.prevResult = new Button("<");
        this.nextResult = new Button(">");
        this.resetView = new Button("Reset");

        // Buttons container
        HBox buttonsContainer = new HBox(8);
        buttonsContainer.getChildren().addAll(this.loadButton, this.findExit, this.prevResult, this.nextResult, this.resetView);

        // Top Text
        inAppTitle = new Text("Maze Walker");
        inAppTitle.setFont(new Font(20));


        // Populating the View
        this.root.setCenter(grid);
        this.root.setBottom(buttonsContainer);
        this.root.setTop(inAppTitle);

    }

    // Fianlly Return the Pane
    public Pane getRoot() {
        return root;
    }
}
