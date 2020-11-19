class Fastlege extends Lege implements Kommuneavtale {

    // Properties
    private int contractNumber;

    // Constructor

    public Fastlege(String newName, int newContract) {
        super(newName);
        this.contractNumber = newContract;
    }

    // Getter Methods

    public int hentAvtalenummer(){
        return this.contractNumber;
    }

    // Setter methods

    public void setContractNumber(int newContract) {
        this.contractNumber = newContract;
    }

    @Override
    public String toString() {
        String s = super.toString();
        return s.substring(0, s.length()-1) + String.format(", Contract Number: %d\n", this.contractNumber);
    }
}
