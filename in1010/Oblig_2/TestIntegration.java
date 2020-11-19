public class TestIntegration {

    // Dummy data
    // Populate Drugs

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
    final double price4 = 104.0;
    final int stregth4 = 4;
    final double newPrice4 = 100.0;

    // Populate recipes

    final double price_militar = 0.0;
    final double price_p = 0.0;
    final double price_b = 25.0;
    final int defaultPatientID = 5;
    final int defaultReit = 2;

    // Populate doctors

    final String doctorName = "House";
    final String doctorNameF = "Caddy";
    final int contractID = 12345;

    // Class declaration
    // Drugs
    Legemiddel l;
    LegemiddelA la;
    LegemiddelB lb;
    LegemiddelC lc;

    // Recipes
    ReseptHvite rh;
    ReseptHviteMilitar rhm;
    ReseptHviteP rhp;
    ReseptBlaa rb;

    // Doctors
    Lege lege;
    Fastlege legeF;


    public TestIntegration() {
        // Drugs objects
        l = new Legemiddel(name1, price1, substance1);
        la = new LegemiddelA(name2, price2, substance2, stregth2);
        lb = new LegemiddelB(name3, price3, substance3, stregth3);
        lc = new LegemiddelC(name4, price4, substance4);

        // Doctor objects
        lege = new Lege(doctorName);
        legeF = new Fastlege(doctorNameF, contractID);

        // Recipe objects
        rh = new ReseptHvite(lc, lege, defaultPatientID, defaultReit);
        rhm = new ReseptHviteMilitar(lc, lege, defaultPatientID, defaultReit);
        rhp = new ReseptHviteP(lc, lege, defaultPatientID, defaultReit);
        rb = new ReseptBlaa(lc, lege, defaultPatientID, defaultReit);

    }

    // Drug testing methods

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

    // Recipe testing methods

    public void testCommonMethodsRecipe (Resept newRecipe) {
        System.out.printf("ID is %d\n", newRecipe.hentId());
        System.out.printf("Recipe colour is %s\n", newRecipe.farge());
        System.out.printf("Drug is %s -> Expected %s\n", newRecipe.hentLegemiddel().hentNavn(), "Paracet");
        System.out.printf("Doctor is %s -> Expected %s\n", newRecipe.hentLege().getName(), doctorName);
        System.out.printf("Patient ID is %d -> Expected %d\n", newRecipe.hentPasientId(), defaultPatientID);
        System.out.printf("Reit is %d -> Expected %d (3 for P-resept)\n", newRecipe.hentReit(), defaultReit);
        if (newRecipe.bruk()) {System.out.println("We used the recipe once.");} else {System.out.println("Recipe is not valid.");}
        System.out.printf("Reit is now %d -> Expected %d (2 for P-resept)\n", newRecipe.hentReit(), (defaultReit - 1));
        if (newRecipe.bruk()) {System.out.println("We used the recipe once.");} else {System.out.println("Recipe is not valid.");}
        System.out.printf("Reit is now %d -> Expected %d (1 for P-resept)\n", newRecipe.hentReit(), (defaultReit - 2));
        if (newRecipe.bruk()) {System.out.println("We used the recipe once.");} else {System.out.println("Recipe is not valid.");}
        System.out.printf("Reit is now %d -> Expected %d\n", newRecipe.hentReit(), (defaultReit - 2));
        System.out.println();
    }

    public void testPricing(Resept newRecipe, double expectedValue) {
        System.out.printf("Recipe type: %s, Price: %.1f, Expected: %.1f\n", newRecipe.getClass(), newRecipe.prisAaBetale(), expectedValue);
    }

    // Doctors testing methods

    public void testDoctrs() {
        System.out.printf("Doctors name is %s -> Expected %s.\n", lege.getName(), doctorName);
        System.out.printf("Doctors (fastlege) name is %s -> Expected %s.\n", legeF.getName(), doctorNameF);
        System.out.printf("Contact ID of the doctor (fastlege): %d -> Expected: %d\n", legeF.hentAvtalenummer(), contractID);
        System.out.println();
    }


    public void testRoutine() {
        System.out.println("We are testing DRUG objects now...");
        checkIDs();
        checkNames();
        checkSubstance();
        checkPrice();
        setNewPrice();
        checkStrength();
        System.out.println("We are testing DOCTOR objects now...");
        testDoctrs();
        System.out.println("We are testing recipe objects now...");
        System.out.println("Testing common recipe methods...");
        System.out.println();
        System.out.printf("Testing %s...\n", rh.getClass());
        testCommonMethodsRecipe(rh);
        System.out.printf("Testing %s...\n", rhm.getClass());
        testCommonMethodsRecipe(rhm);
        System.out.printf("Testing %s...\n", rhp.getClass());
        testCommonMethodsRecipe(rhp);
        System.out.printf("Testing %s...\n", rb.getClass());
        testCommonMethodsRecipe(rb);
        System.out.println("Testing price calculation...");
        testPricing(rhm, price_militar);
        testPricing(rhp, price_p);
        testPricing(rb, price_b);
    }

    public static void main(String[] args) {
        TestIntegration test = new TestIntegration();
        test.testRoutine();
    }

}
