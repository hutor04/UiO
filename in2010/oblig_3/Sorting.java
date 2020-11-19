import java.util.Arrays;
import java.util.Comparator;
import java.util.Random;

public class Sorting {

    //Swapper
    public static void swap(int[] input, int a, int b) {
        int temp = input[a];
        input[a] = input[b];
        input[b] = temp;
    }

    //Input data generator
    public static int[] dataGenerator(int num, int min, int max, int type) {
        int[] result;

        if (type == 2) {
            result = new Random().ints(num, min, max).toArray(); // Shuffled
        } else if (type == 0) {
            result = new Random().ints(num, min, max).sorted().toArray(); // Sorted
        } else {
            result = new Random().ints(num, min, max).sorted().toArray(); // Reverse
            for (int i = 0; i < num/2; i++) {
                Sorting.swap(result, i, num - i - 1);
            }
        }
        return result;
    }

    // Helper Methods. Generates pretty array print
    public static void resultsPrinter(int[] input) {
        String output;
        StringBuilder arr = new StringBuilder();

        for (int i = 0; i < input.length; i++) {
            arr.append(input[i] + ", ");
        }
        output = (arr.length() > 3) ? arr.substring(0, arr.length() - 2) : arr.toString();
        System.out.println("[" + output + "]");

    }

    // Selection sort algo implementation
    public static void SelectionSort(int[] input, Comparator<Integer> comp, boolean verbose) {
        for (int i = 0; i < input.length; i++) {
            int currMin = i;
            for (int j = i + 1; j < input.length; j++) {
                if (comp.compare(input[j], input[currMin]) < 0) {
                    currMin = j;
                }
            }
            if (i != currMin) {
                Sorting.swap(input, i, currMin);
            }
            if (verbose) {
                Sorting.resultsPrinter(input);
            }
        }
    }

    // Insertion sort algorithm implementation with subarray support
    public static void InsertionSort(int[] input, int a, int b, Comparator<Integer> comp, boolean verbose) {
        for (int i = a + 1; i <= b; i++) {
            int currentElement = input[i];

            int j = i;

            while (j > a && comp.compare(currentElement, input[j - 1]) < 0) {
                input[j] = input[j - 1];
                j--;
            }
            input[j] = currentElement;

            if (verbose) {
                Sorting.resultsPrinter(input);
            }
        }

    }

    // Quick sort algorithm implementation
    private static int inPlacePartition(int[] input, int a, int b, Comparator<Integer> comp) {
        Random random = new Random();
        int r = random.nextInt((b - a) + 1) + a; // Random number from a to b
        Sorting.swap(input, r, b); // Swap input[r] and input[b]

        int p = input[b]; // Pivot
        int l = a; // Rightward scan
        r = b - 1; // Leftward scan
        while (l <= r) {
            while (l <= r && comp.compare(input[l], p) <= 0 ) {
                l++;
            }
            while (r >= l && comp.compare(input[r], p) >= 0) {
                r--;
            }
            if (l < r) {
                Sorting.swap(input, l, r);
            }
        }
        Sorting.swap(input, l, b);
        return l;
     }

    public static void inPlaceQuickSort(int[] input, int a, int b, Comparator<Integer> comp, boolean verbose) {

        while (a < b) {
            int l = inPlacePartition(input, a , b, comp);
            if (l - a < b - l) {
                inPlaceQuickSort(input, a, l - 1, comp,verbose);
                a = l + 1;
            } else {
                inPlaceQuickSort(input, l + 1, b, comp, verbose);
                b = l - 1;
            }
            if (verbose) {
                Sorting.resultsPrinter(input);
            }

        }

    }

    // Runs Insertion sort if the sub-task is less than 10 elements
    public static void inPlaceQuickSortWithInsertionSort(int[] input, int a, int b, Comparator<Integer> comp,
                                                         boolean verbose) {
        if (a < b) {
            if ((b - a) < 9) {
                Sorting.InsertionSort(input, a, b, comp, verbose);
            } else {
                int l = inPlacePartition(input, a , b, comp);
                inPlaceQuickSortWithInsertionSort(input, a, l-1, comp, verbose);
                inPlaceQuickSortWithInsertionSort(input, l + 1, b, comp, verbose);
            }
        }

    }

    // Bucket sort algorithm implmentation
    public static void  bucketSort(int[] input, int min, int max, boolean verbose) {
        // It doesn't support comparator

        int[] result = new int[input.length]; // Sorted array
        int[] pos = new int[max + 1]; // Container for positive numbers
        Arrays.fill(pos, -1);
        int[] neg = null; // Container for negative numbers

        // Initiate neg container if necessary
        if (min < 0) {
            neg = new int[-1 * min + 1];
            Arrays.fill(neg, 0);
        }
        // Fill the containers
        for (int i = 0; i < input.length; i++) {
            int current = input[i];

            if (current >= 0) {
                pos[current]++;
            } else {
                neg[-1 * current]++;
            }
        }
        int cursor = 0;
        // Rebuild negative
        if (neg != null) {
            for (int i = neg.length - 1; i >= 0; i--) {
                if (neg[i] != 0) {
                    while (neg[i] > 0) {
                        input[cursor] = -1 * i;
                        cursor++;
                        neg[i]--;
                        if (verbose) {
                            Sorting.resultsPrinter(input);
                        }
                    }
                }
            }
            neg = null; // Free memory
        }
        // Rebuild positive
        for (int i = 0; i < pos.length; i++) {
            if (pos[i] != -1) {
                while (pos[i] >= 0) {
                    input[cursor] = i;
                    cursor++;
                    pos[i]--;
                    if (verbose) {
                        Sorting.resultsPrinter(input);
                    }
                }
            }
        }
    }



}
