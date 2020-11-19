import java.util.ArrayList;

// Edited for testing the Generic tree
// Added 'clear' action so that a new tree is created (antall == 0 case)

class BSTtest {

    public static ArrayList<Integer> tallrekke( int antall ) {
        ArrayList<Integer> results = new ArrayList<>();
        java.util.Random tilf = new java.util.Random(20102018);
        for ( int i=0; i<antall; i++) {
            results.add(tilf.nextInt());
        }
        return results;
    }


    public static void main(String[] args) {

        int antall = Integer.parseInt(args[0]);

        ArrayList<Integer> intarr = tallrekke(antall);
        BSTree<Integer> testtre = new BSTree<>();

        if (antall == 0 ) {

            System.out.println("n     antall     høyde");
            for (int ant=1; ant <= 100000000; ant=ant*10) {
                intarr = tallrekke(ant);
                for (Integer i : intarr) {testtre.add(i);}
                System.out.print(ant);
                System.out.print(" " + testtre.size());
                System.out.println(" " + testtre.height());
                testtre.clearTree(); // Clear the tree.
            }

        }
        else {

            for (Integer i : intarr) { testtre.add(i); }
            intarr = testtre.preorderArray();
            for (int i : intarr) { System.out.println(i); }
            intarr = testtre.sortedArray();
            for (int i : intarr) { System.out.println(i); }
        }
    }
}