public class Aapning extends HvitRute {


    // Constructor
    public Aapning(Labyrint newHost, int newRow, int newCol) {
        super(newHost, newRow, newCol);
    }


    // Cell status exit or not
    @Override
    public boolean isExit() {
        return true;
    }
}
