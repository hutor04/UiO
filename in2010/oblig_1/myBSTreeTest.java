import java.util.ArrayList;

class myBSTreeTest {
    public static void main(String[] args) {
        BSTree<Integer> t = new BSTree<>();
        // Testing add
        t.add(30);
        t.add(40);
        t.add(50);
        t.add(24);
        t.add(8);
        t.add(58);
        t.add(48);

        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(26);
        arr.add(11);
        arr.add(13);

        // Testing add all
        t.addAll(arr);


        // Find parent
        System.out.println("Testing find parent");
        System.out.println(t.findParent(13)); // Should be 11
        System.out.println("Testing find grandparent");
        System.out.println(t.findGrandparent(13)); // Should be 8

        // Find node
        System.out.println("Find non-existent node");
        System.out.println(t.find(100)); // Returns null
        System.out.println("Find node");
        System.out.println(t.find(13)); // Prints node

        // Remove node
        System.out.println("Print in order before node removal");
        t.printInOrder();
        t.remove(8);
        System.out.println("Print in order after removing 8");
        t.printInOrder();
        System.out.println("Tree size");
        System.out.println(t.size());
        System.out.println("Tree height");
        System.out.println(t.height());
        System.out.println("Check if value exists (non-existent)");
        System.out.println(t.existsInTree(8)); // returns false
        System.out.println("Check if value exists");
        System.out.println(t.existsInTree(13)); // returns true
        System.out.println("Find nearest smallest (input 15)");
        System.out.println(t.findNearestSmallerThan(15)); //13 expected
        System.out.println("Find in range 5-15");
        System.out.println(t.findInRange(5, 15)); // 11-13 expected

        // Testing RB tree
        RBTree<Integer> rbt = new RBTree<>();
        // Testing add
        rbt.add(30);
        rbt.add(40);
        rbt.add(50);
        rbt.add(24);
        rbt.add(8);
        rbt.add(58);
        rbt.add(48);

        // Testing add all
        rbt.addAll(arr);

        System.out.println("Check if valid");
        System.out.println(rbt.isValidRebBlack());
        System.out.println("Printing in order");
        rbt.printInOrder();
        System.out.println("Printing after removal of node 30");
        t.remove(30);
        rbt.printInOrder();
        System.out.println("Is the tree valid?");
        System.out.println(rbt.isValidRebBlack());


    }
}
