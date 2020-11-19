public class TestResepter {

    final double price_militar = 0.0;
    final double price_p = 0.0;
    final double price_b = 25.0;

    final String doctorName = "House";

    final int defaultPatientID = 5;
    final int defaultReit = 2;

    Lege lege;
    ReseptHvite rh;
    ReseptHviteMilitar rhm;
    ReseptHviteP rhp;
    ReseptBlaa rb;


    public TestResepter(TestLegemiddel testCase1) {
        lege = new Lege(doctorName);
        rh = new ReseptHvite(testCase1.lc, lege, defaultPatientID, defaultReit);
        rhm = new ReseptHviteMilitar(testCase1.lc, lege, defaultPatientID, defaultReit);
        rhp = new ReseptHviteP(testCase1.lc, lege, defaultPatientID, defaultReit);
        rb = new ReseptBlaa(testCase1.lc, lege, defaultPatientID, defaultReit);
    }

    public void testCommonMethods(Resept newRecipe) {
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

    public void testRoutine() {
        System.out.println("Initiating recipe objects...");
        System.out.println("Testing common recipe methods...");

        System.out.printf("Testing %s...\n", rh.getClass());
        testCommonMethods(rh);

        System.out.printf("Testing %s...\n", rhm.getClass());
        testCommonMethods(rhm);

        System.out.printf("Testing %s...\n", rhp.getClass());
        testCommonMethods(rhp);

        System.out.printf("Testing %s...\n", rb.getClass());
        testCommonMethods(rb);

        System.out.println("Testing price calculation...");

        testPricing(rhm, price_militar);
        testPricing(rhp, price_p);
        testPricing(rb, price_b);

    }

    public static void main(String[] args) {
        TestLegemiddel test1 = new TestLegemiddel();
        TestResepter test2 = new TestResepter(test1);
        test2.testRoutine();
    }
}
