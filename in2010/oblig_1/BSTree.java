import java.util.ArrayList;
import java.util.Collections;

public class BSTree<T extends Comparable<T>> implements BSTOper<T> {
    // BSTree data.
    protected Node root;
    protected int size;

    // Node class
    protected class Node {
        // Parent added for quicker operation
        Node left, right, parent;
        T value;

        Node() {} // I'm using null pointers
        Node(Node parent, T v) {
            this.value = v;
            this.parent = parent;
        }

        // Helper methods
        protected boolean hasLeftChild() {
            return this.left != null;
        }

        protected boolean hasRightChild() {
            return this.right != null;
        }

        protected boolean isLeftChild() {
            return this.parent != null && this.parent.left == this;
        }

        protected boolean isRoot() {
            return this.parent == null;
        }

        protected boolean isLeaf() {
            return this.right == null && this.left == null;
        }

        protected Node getGrandParent() {
            return this.parent.parent;
        }

        protected Node getSibling() {
            if (!this.isRoot()) {
                if (this.isLeftChild()) {
                    return this.parent.right;
                } else {
                    return this.parent.left;
                }

            } else {
                return null;
            }
        }

        @Override
        public String toString() {
            return String.format("%s", this.value);
        }
    }

    // BSTree class constructor.
    public BSTree() {
        root = null;
        size = 0;
    }

    // Find parent. It doesn't rely on the link to the node's parent.
    private Node findParent(Node n) {
        ArrayList<Node> parents = new ArrayList<>();
        _search(this.root, n.value, parents);
        if (parents.size() == 0) {
            return null;
        } else {
            return parents.get(parents.size() - 1);
        }
    }

    // Helper method implemented for testing.
    public Node findParent(T n) {
        ArrayList<Node> parents = new ArrayList<>();
        _search(this.root, n, parents);
        if (parents.size() == 0) {
            return null;
        } else {
            return parents.get(parents.size() - 1);
        }
    }

    // Find grandparent. It doesn't rely on the link to the node's parent.
    private Node findGrandparent(Node n) {
        ArrayList<Node> parents = new ArrayList<>();
        _search(this.root, n.value, parents);
        if (parents.size() < 2) {
            return null;
        } else {
            return parents.get(parents.size() - 2);
        }
    }

    // Helper method implemented for testing.
    public Node findGrandparent(T n) {
        ArrayList<Node> parents = new ArrayList<>();
        _search(this.root, n, parents);
        if (parents.size() < 2) {
            return null;
        } else {
            return parents.get(parents.size() - 2);
        }
    }


    // Find Node.
    public Node find(T value) {
        return _search(this.root, value);
    }

    // Search (Helper method).
    private Node _search(Node node, T value) {
        if (value.compareTo(node.value) == 0) {
            return node;
        } else if (value.compareTo(node.value) < 0) {
            if (node.hasLeftChild()) {
                return _search(node.left, value);
            } else {
                return null;
            }
        } else if (value.compareTo(node.value) > 0) {
            if (node.hasRightChild()) {
                return _search(node.right, value);
            } else {
                return null;
            }
        } else {
            return null;
        }
    }

    // Overloaded search (Helper method). It is used for parents search.
    private void _search(Node node, T value, ArrayList<Node> accumulator) {
        if (value.compareTo(node.value) == 0) {
            return;
        } else if (value.compareTo(node.value) < 0) {
            if (node.hasLeftChild()) {
                accumulator.add(node);
                _search(node.left, value, accumulator);
            } else {
                return;
            }
        } else if (value.compareTo(node.value) > 0) {
            if (node.hasRightChild()) {
                accumulator.add(node);
                _search(node.right, value, accumulator);
            } else {
                return;
            }
        } else {
            return;
        }
    }
    // Find END

    // Insertion.
    public void add(T value) {
        if (this.root != null) {
            _add(this.root, value);
        } else {
            this.root = new Node(null, value);
        }
        this.size += 1;
    }

    // Add all items from the array.
    public void addAll(ArrayList<T> values) {
        for (T v: values){
            add(v);
        }
    }

    // Add helper method.
    protected void _add(Node node, T value) {
        if (value.compareTo(node.value) < 0) {
            if (node.hasLeftChild()) {
                _add(node.left, value);
            } else {
                node.left = new Node(node, value);
            }
        } else {
            if (node.hasRightChild()) {
                _add(node.right, value);
            } else {
                node.right = new Node(node, value);
            }
        }

    }
    // Insertion END

    // Deletion (it uses pointers for brevity, but we can well use implemented findParent methods instead)
    public boolean remove(T value) {
        Node nodeToRemove = _search(this.root, value);

        if (nodeToRemove == null) {
            return false;
        } else {
            if (nodeToRemove.left == null) {
                _substituteOneExternal(nodeToRemove, nodeToRemove.right);
            } else if (nodeToRemove.right == null) {
                _substituteOneExternal(nodeToRemove, nodeToRemove.left);
            } else {
                Node temp = _min(nodeToRemove.right);
                _substituteOneExternal(temp, temp.right);
                nodeToRemove.value = temp.value;
            }
            this.size -= 1;
            return true;
        }
    }

    private void _substituteOneExternal(Node nodeToRemove, Node substitute) {
        if (nodeToRemove.isLeftChild()) {
            nodeToRemove.parent.left = substitute;
        } else {
            nodeToRemove.parent.right = substitute;
        }
    }
    // Deletion END

    // Get Size
    public int size() {
        //ArrayList<Node> nodes = new ArrayList<>();
        //_inOrderTraversal(this.root, nodes);
        return this.size;
    }
    // Get Size END

    // Get height
    public int height() {
        return _height(this.root);
    }

    private int _height(Node node) {
        int height = 0;

        if (node.hasLeftChild()) {
            height = Math.max(height, 1 + _height(node.left));
        }
        if (node.hasRightChild()) {
            height = Math.max(height, 1 + _height(node.right));
        }
        return height;
    }
    // Get height END

    // Check if Key exists
    public boolean existsInTree(T value) {
        return _search(this.root, value) != null;
    }
    // Check if Key exists END

    // Find the next smallest value
    public T findNearestSmallerThan(T value) {
        return _findNearestSmallerThan(this.root, value);

    }

    private T _findNearestSmallerThan(Node node, T value) {
        if (node == null) {
            return null;
        }

        ArrayList<T> result = new ArrayList<>();

        if (node.value.compareTo(value) < 0) {
            result.add(node.value);
        }

        T left = _findNearestSmallerThan(node.left, value);
        T right = _findNearestSmallerThan(node.right, value);

        if (left != null) {
            result.add(left);
        }

        if (right != null) {
            result.add(right);
        }


        if (result.size() > 0) {
            return Collections.max(result);
        } else {
            return null;
        }
    }

    // Find minimum value (Helper method).
    private Node _min(Node node) {
        if (node.left == null) {
            return node;
        } else {
            return _min(node.left);
        }
    }
    // Find the next smallest value END

    public ArrayList<T> sortedArray() {
        ArrayList<Node> nodes = new ArrayList<>();
        ArrayList<T> result = new ArrayList<>();
        _inOrderTraversal(this.root, nodes);
        for (Node n: nodes) {
            result.add(n.value);
        }
        return result;
    }

    public ArrayList<T> preorderArray() {
        ArrayList<Node> nodes = new ArrayList<>();
        ArrayList<T> result = new ArrayList<>();
        _preOrderTraversal(this.root, nodes);
        for (Node n: nodes) {
            result.add(n.value);
        }
        return result;

    }


    // Finds values in the tree inclusive the given values
    public ArrayList<T> findInRange (T low, T high) {
        ArrayList<Node> nodes = new ArrayList<>();
        ArrayList<T> result = new ArrayList<>();
        // Set last argument to 0 for exclusive search
        _findInRange(this.root, low, high, nodes, 1);
        for (Node n: nodes) {
            result.add(n.value);
        }
        return result;
    }

    // Find in range (Helper method).
    private void _findInRange(Node node, T low, T high, ArrayList<Node> accumulator, int mode) {
        if (node == null) {
            return;
        }
        if (low.compareTo(node.value) < 0) {
            _findInRange(node.left, low, high, accumulator, mode);
        }
        if (mode == 1) {
            if (low.compareTo(node.value) <= 0 && high.compareTo(node.value) >= 0) {
                accumulator.add(node);
            }
        } else {
            if (low.compareTo(node.value) < 0 && high.compareTo(node.value) > 0) {
                accumulator.add(node);
            }
        }
        if (high.compareTo(node.value) > 0) {
            _findInRange(node.right, low, high, accumulator, mode);
        }
    }

    // In order traversal (Helper method)
    protected void _inOrderTraversal(Node node, ArrayList<Node> accumulator) {
        if (node.hasLeftChild()) {
            _inOrderTraversal(node.left, accumulator);
        }
        accumulator.add(node);
        if (node.hasRightChild()) {
            _inOrderTraversal(node.right, accumulator);
        }
    }

    protected void _preOrderTraversal(Node node, ArrayList<Node> accumulator) {
        accumulator.add(node);

        if (node.hasLeftChild()) {
            _preOrderTraversal(node.left, accumulator);
        }

        if (node.hasRightChild()) {
            _preOrderTraversal(node.right, accumulator);
        }
    }

    // Helper for debugging
    public void printInOrder() {
        ArrayList<Node> nodes = new ArrayList<>();
        _inOrderTraversal(this.root, nodes);
        for (Node n: nodes) {
            System.out.println(n);
        }
    }


    // Node Rotation (Helper Methods)
    protected void _rotateAboveParent(Node node) {
        if (node.isLeftChild()) {
            _rotateRight(node);
        } else {
            _rotateLeft(node);
        }
    }

    private void _rotateRight(Node node) {
        Node parent = node.parent;
        Node rightSubTree = node.right;
        Node grandParent = node.getGrandParent();

        if (grandParent == null) {
            this.root = node;
            node.parent = null;

            parent.parent = node;
            if (node.right != null) {
                parent.left = node.right;
                node.right.parent = parent;
            } else {
                parent.left = null;
            }
            node.right = parent;

        } else {
            // Reconnect with grandparent
            if (parent.isLeftChild()) {
                grandParent.left = node;
                node.parent = grandParent;
            } else {
                grandParent.right = node;
                node.parent = grandParent;
            }

            // Reconnect with former parent
            node.right = parent;
            parent.parent = node;

            parent.left = rightSubTree;
            if (rightSubTree != null) {
                rightSubTree.parent = parent;
            }

        }
    }


    private void _rotateLeft(Node node) {
        Node parent = node.parent;
        Node leftSubTree = node.left;
        Node grandParent = node.getGrandParent();

        if (grandParent == null) {
            this.root = node;
            node.parent = null;

            parent.parent = node;

            if (node.left != null) {
                parent.right = node.left;
                node.left.parent = parent;
            } else {
                parent.right = null;
            }

            node.left = parent;

        }

        else {
            // Reconnect with grandparent
            if (parent.isLeftChild()) {
                grandParent.left = node;
                node.parent = grandParent;
            } else {
                grandParent.right = node;
                node.parent = grandParent;
            }

            // Reconnect with former parent
            node.left = parent;
            parent.parent = node;

            parent.right = leftSubTree;
            if (leftSubTree != null) {
                leftSubTree.parent = parent;
            }
        }
    }

    // Delete all nodes.
    public void clearTree() {
        ArrayList<Node> nodes = new ArrayList<>();
        _inOrderTraversal(this.root, nodes);
        for (Node n: nodes) {
            n.left = null;
            n.right = null;
            n.parent = null;
        }

        this.root = null;
        this.size = 0;
     }


}
