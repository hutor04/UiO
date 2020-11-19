import java.util.Arrays;
import java.util.Comparator;

public class TestSorting {

    public static double testAlgos2(int num, int min, int max, int sequenceType, Comparator<Integer> comp,
                                  boolean verbose) {
        long startTime;
        long endTime;
        double elapsed;
        int[] a;

        a = Sorting.dataGenerator(num, min, max, sequenceType);
        startTime = System.nanoTime();
        Sorting.bucketSort(a, min, max, verbose);
        endTime = System.nanoTime();
        elapsed = (endTime - startTime) / 10000000.0;
        //System.out.println("Runtime (ms): " + elapsed + "\n");
        return elapsed;

    }

    public static void testAlgos(int num, int min, int max, int sequenceType, Comparator<Integer> comp,
                                 boolean verbose) {
        long startTime;
        long endTime;
        double elapsed;
        int[] a;

        System.out.println(">>> Size: " + num);
        if (sequenceType == 0) {
            System.out.println(">>> Testing Sorted Array:");
        } else if (sequenceType == 1) {
            System.out.println(">>> Testing Reversed Array:");
        } else {
            System.out.println(">>> Testing Shuffled Array:");
        }

        System.out.println("Testing Selection Sort:");
        a = Sorting.dataGenerator(num, min, max, sequenceType);
        //System.out.print("INPUT:");
        //Sorting.resultsPrinter(a);
        startTime = System.nanoTime();
        Sorting.SelectionSort(a, comp, verbose);
        endTime = System.nanoTime();
        elapsed = (endTime - startTime) / 10000000.0;
        System.out.println("Runtime (ms): " + elapsed + "\n");

        System.out.println("Testing Insertion Sort:");
        a = Sorting.dataGenerator(num, min, max, sequenceType);
        //System.out.print("INPUT:");
        //Sorting.resultsPrinter(a);
        startTime = System.nanoTime();
        Sorting.InsertionSort(a, 0, num - 1, comp, verbose);
        endTime = System.nanoTime();
        elapsed = (endTime - startTime) / 10000000.0;
        System.out.println("Runtime (ms): " + elapsed + "\n");

        System.out.println("Testing Quick Sort:");
        a = Sorting.dataGenerator(num, min, max, sequenceType);
        //System.out.print("INPUT:");
        //Sorting.resultsPrinter(a);
        startTime = System.nanoTime();
        Sorting.inPlaceQuickSort(a, 0, a.length - 1, comp, verbose);
        endTime = System.nanoTime();
        elapsed = (endTime - startTime) / 10000000.0;
        System.out.println("Runtime (ms): " + elapsed + "\n");

        System.out.println("Testing Quick Sort with Insertion Sort:");
        a = Sorting.dataGenerator(num, min, max, sequenceType);
        //System.out.print("INPUT:");
        //Sorting.resultsPrinter(a);
        startTime = System.nanoTime();
        Sorting.inPlaceQuickSortWithInsertionSort(a, 0, a.length - 1, comp, verbose);
        endTime = System.nanoTime();
        elapsed = (endTime - startTime) / 10000000.0;
        System.out.println("Runtime (ms): " + elapsed + "\n");

        System.out.println("Testing Bucket Sort:");
        a = Sorting.dataGenerator(num, min, max, sequenceType);
        //System.out.print("INPUT:");
        //Sorting.resultsPrinter(a);
        startTime = System.nanoTime();
        Sorting.bucketSort(a, min, max, verbose);
        endTime = System.nanoTime();
        elapsed = (endTime - startTime) / 10000000.0;
        System.out.println("Runtime (ms): " + elapsed + "\n");

        System.out.println("Testing Arrays.sort Sort:");
        a = Sorting.dataGenerator(num, min, max, sequenceType);
        //System.out.print("INPUT:");
        //Sorting.resultsPrinter(a);
        startTime = System.nanoTime();
        Arrays.sort(a);
        endTime = System.nanoTime();
        elapsed = (endTime - startTime) / 10000000.0;
        System.out.println("Runtime (ms): " + elapsed + "\n");



    }

    public static void main(String[] args) {
        // Demo
        int num = 10;
        int min = -10;
        int max = 10;

        // Speed
        int[] speed_input = {1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 50000};

        Comparator<Integer> comp = (x, y) -> x.compareTo(y);

        // Demo Test
        TestSorting.testAlgos(num, min, max, 2, comp, true);
        TestSorting.testAlgos(num, min, max, 0, comp, true);
        TestSorting.testAlgos(num, min, max, 1, comp, true);

        // Speed Test
        for (int i = 0; i < speed_input.length; i++) {
            TestSorting.testAlgos(speed_input[i], -1 * speed_input[i], speed_input[i], 2, comp, false);
            TestSorting.testAlgos(speed_input[i], -1 * speed_input[i], speed_input[i], 0, comp, false);
            TestSorting.testAlgos(speed_input[i], -1 * speed_input[i], speed_input[i], 1, comp, false);

            /*
            double[] results = new double[10];
            for (int j = 0; j < 10; j++) {
                System.out.print(j + " ");
                results[j] = TestSorting.testAlgos2(speed_input[i], -1000000, 1000000, 2, comp, false);

            }
            System.out.println("Size: " + speed_input[i]);
            Arrays.stream(results).average().ifPresent(System.out::println);
            System.out.println("========");*/


        }

    }
}
