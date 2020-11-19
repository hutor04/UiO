class Node {
    private int antProc;
    private int antMem;

    public Node(int processors, int memory) {
        antProc = processors;
        antMem = memory;
    }

    public int antProsessorer() {
        return antProc;
    }

    public int antMem() {
        return antMem;
    }

}
