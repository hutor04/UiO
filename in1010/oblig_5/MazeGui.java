import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.File;
import java.io.FileNotFoundException;

public class MazeGui extends Application {
    @Override
    public void start(Stage currentStage) {
        MazeView view = new MazeView(currentStage);
        GuiController controls = new GuiController(currentStage, view);
        Scene scene = new Scene(view.getRoot());
        currentStage.setScene(scene);
        currentStage.setTitle("Oblig 7");
        currentStage.show();

    }
    public static void main(String[] args) {
        Application.launch();
    }
}
