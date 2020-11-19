import java.util.ArrayList;

class Rack {
    private ArrayList<Node> rackList = new ArrayList<>();

    public void settInnNode(Node node) {
        rackList.add(node);
    }

    public int noderiRack() {
        return rackList.size();
    }

    public int prosessoreriRack() {
        int prosessorer = 0;
        if (rackList.size() > 0) {
            for (Node node: rackList) {
                processors += node.antProsessorer();
            }
        }
        return prosessorer;
    }

    public int noderMedNokMinne(int mem) {
        int noder = 0;
        if (rackList.size() > 0) {
            for (Node node: rackList) {
                if (node.antMem() >= mem) {
                    noder++;
                }
            }
        }
        return noder;
    }

}
