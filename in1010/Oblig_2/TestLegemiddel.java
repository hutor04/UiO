public class TestLegemiddel {

    final String name1 = "Aspirin";
    final double substance1 = 501.0;
    final double price1 = 101.0;
    final double newPrice1 = 10101.0;

    final String name2 = "Methadone";
    final double substance2 = 502.0;
    final double price2 = 102.0;
    final int stregth2 = 2;
    final double newPrice2 = 10102.0;

    final String name3 = "Tramadol";
    final double substance3 = 503.0;
    final double price3 = 103.0;
    final int stregth3 = 3;
    final double newPrice3 = 10103.0;

    final String name4 = "Paracet";
    final double substance4 = 504.0;
    final double price4 = 100.0;
    final int stregth4 = 4;
    final double newPrice4 = 10104.0;

    Legemiddel l;
    LegemiddelA la;
    LegemiddelB lb;
    LegemiddelC lc;


    public TestLegemiddel() {
        l = new Legemiddel(name1, price1, substance1);
        la = new LegemiddelA(name2, price2, substance2, stregth2);
        lb = new LegemiddelB(name3, price3, substance3, stregth3);
        lc = new LegemiddelC(name4, price4, substance4);

    }

    public void checkIDs() {
        System.out.printf("ID is %d -> Expected 0\n", l.hentId());
        System.out.printf("ID is %d -> Expected 1\n", la.hentId());
        System.out.printf("ID is %d -> Expected 2\n", lb.hentId());
        System.out.printf("ID is %d -> Expected 3\n", lc.hentId());
        System.out.println();
    }

    public void checkNames() {
        System.out.printf("Name is %s -> Expected %s\n", l.hentNavn(), name1);
        System.out.printf("Name is %s -> Expected %s\n", la.hentNavn(), name2);
        System.out.printf("Name is %s -> Expected %s\n", lb.hentNavn(), name3);
        System.out.printf("Name is %s -> Expected %s\n", lc.hentNavn(), name4);
        System.out.println();
    }

    public void checkSubstance() {
        System.out.printf("Substance is %.1f -> Expected %.1f\n", l.hentVirkestoff(), substance1);
        System.out.printf("Substance is %.1f -> Expected %.1f\n", la.hentVirkestoff(), substance2);
        System.out.printf("Substance is %.1f -> Expected %.1f\n", lb.hentVirkestoff(), substance3);
        System.out.printf("Substance is %.1f -> Expected %.1f\n", lc.hentVirkestoff(), substance4);
        System.out.println();
    }

    public void checkPrice() {
        System.out.printf("Price is %.1f -> Expected %.1f\n", l.hentPris(), price1);
        System.out.printf("Price is %.1f -> Expected %.1f\n", la.hentPris(), price2);
        System.out.printf("Price is %.1f -> Expected %.1f\n", lb.hentPris(), price3);
        System.out.printf("Price is %.1f -> Expected %.1f\n", lc.hentPris(), price4);
        System.out.println();
    }

    public void setNewPrice() {
        l.settNyPris(newPrice1);
        la.settNyPris(newPrice2);
        lb.settNyPris(newPrice3);
        lc.settNyPris(newPrice4);
        System.out.printf("New price is %.1f -> Expected %.1f\n", l.hentPris(), newPrice1);
        System.out.printf("New price is %.1f -> Expected %.1f\n", la.hentPris(), newPrice2);
        System.out.printf("New price is %.1f -> Expected %.1f\n", lb.hentPris(), newPrice3);
        System.out.printf("New price is %.1f -> Expected %.1f\n", lc.hentPris(), newPrice4);
        System.out.println();
    }

    public void checkStrength() {
        System.out.printf("Strength is %d -> Expected %d\n", la.hentNarkotiskStyrke(), stregth2);
        System.out.printf("Strength is %d -> Expected %d\n", lb.hentVanedannendeStyrke(), stregth3);
        System.out.println();
    }

    public void testRoutine() {
        checkIDs();
        checkNames();
        checkSubstance();
        checkPrice();
        setNewPrice();
        checkStrength();
    }

    public static void main(String[] args) {
        TestLegemiddel test = new TestLegemiddel();
        test.testRoutine();
    }

}
