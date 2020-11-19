import java.util.ArrayList;
import java.io.File;
import java.util.Scanner;

class Regneklynge {
    private ArrayList<Rack> regneklynge = new ArrayList<>();
    private int noderPerRack;


    public Regneklynge(String file) throws Exception {
        Rack rack = new Rack();
        regneklynge.add(rack);

        Scanner in = new Scanner(new File(file));
        while (in.hasNextLine()) {
            String nextLine = in.nextLine();
            String[] deler = nextLine.split(" ");

            if (deler.length == 1) {
                this.noderPerRack = Integer.parseInt(deler[0]);

            } else {
                int quantity = Integer.parseInt(deler[0]);
                int memory = Integer.parseInt(deler[1]);
                int processors = Integer.parseInt(deler[2]);

                for (int i = 0; i < quantity; i++) {
                    this.settInnNode(new  Node(processors, memory));
                }
            }

        }

    }

    public void settInnNode(Node node) {
        Rack sisteElement = regneklynge.get(regneklynge.size()-1);

        if (sisteElement.noderiRack() < noderPerRack) {
            sisteElement.settInnNode(node);

        } else {
            Rack rack = new Rack();
            regneklynge.add(rack);
            rack.settInnNode(node);
        }
    }


}

    public int antRacks() {
        return regneklynge.size();
    }

    public int antProsessorer() {
        int prosessorer = 0;
        if (regneklynge.size() > 0) {
            for (Rack rack : regneklynge) {
                processors += rack.prosessoreriRack();
            }
        }
        return prosessorer;
    }

    public int noderMedNokMinne(int memory) {
        int nodes = 0;
        if (regneklynge.size() > 0) {
            for (Rack rack : regneklynge) {
                nodes += rack.noderMedNokMinne(memory);
            }
        }
        return nodes;
    }

}