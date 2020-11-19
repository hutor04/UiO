import javafx.event.EventHandler;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Rectangle;
import javafx.scene.paint.Color;

// My Rectangle
class myRectangle extends Rectangle {
    private Paint myColor;
    private boolean selected = false;
    private Rute mazeCell;

    public myRectangle(int width, int height, Rute newMazeCell) {
        super(width, height);
        this.myColor = newMazeCell.isWall() ?  Color.BLACK : Color.WHITE;
        super.setFill(this.myColor);
        this.mazeCell = newMazeCell;
        this.setOnMouseEntered(new HoverOverCell(this));
        this.setOnMouseExited(new ExitHoverOverCell(this));
    }

    public Paint getColor() {
        return this.myColor;
    }

    public Rute getCell() {
        return this.mazeCell;
    }

    public void select() {
        this.selected = true;
        this.setFill(Color.RED);
    }

    public void deSelect() {
        this.selected = false;
        this.setFill(this.myColor);
    }

    public boolean isSelected() {
        return this.selected;
    }

    // Hover handler
    class HoverOverCell implements EventHandler<MouseEvent> {
        myRectangle f;
        public HoverOverCell(myRectangle field) {
            f = field;
        }
        @Override
        public void handle(MouseEvent event) {
            f.setFill(Color.GREEN);
        }
    }

    // Hover out handler
    class ExitHoverOverCell implements EventHandler<MouseEvent> {
        myRectangle f;
        public ExitHoverOverCell(myRectangle field) {
            f = field;
        }
        @Override
        public void handle(MouseEvent event) {
            if (f.isSelected()) {
                f.setFill(Color.RED);
            } else {
                f.setFill(f.getColor());
            }

        }
    }


}