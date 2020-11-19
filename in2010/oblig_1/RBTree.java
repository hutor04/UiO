import java.util.ArrayList;
import java.util.Collections;

public class RBTree<T extends Comparable<T>> extends BSTree<T> {
    // Color codes.
    private static byte BLACK = 1;
    private static byte RED = 2;

    // Red-Black Tree Node class
    public class RBNode extends Node {
        RBNode(RBNode parent, T value) {
            super(parent, value);
        }

        private byte colour = 0;

        private boolean isRed() {
            return colour == RED;
        }
        private boolean isBlack() {
            return colour == BLACK;
        }

        public void setToRed() {
            colour = RED;
        }
        public void setToBlack() {
            colour = BLACK;
        }

        public String toString() {
            String col = (this.colour == RED) ? "R" : "B";
            return String.format("(%s, %s)", this.value, col);
        }
    }

    // Red-Black Tree Insertion
    public void add(T value) {
        if (this.root != null) {
            _add(this.root, value);
        } else {
            this.root = new RBNode(null, value);
            RBNode rootRB = (RBNode) this.root;
            // Root is always black
            rootRB.setToBlack();
        }
        this.size += 1;
    }

    // Check Red-Black properties
    public boolean isValidRebBlack() {
        boolean result = true;
        // Check if root is Black
        if (((RBNode) this.root).colour != BLACK) {
            result = false;
        }

        // Check if RED nodes have black parents
        ArrayList<Node> nodes = new ArrayList<>();
        _inOrderTraversal(this.root, nodes);
        for (Node n: nodes) {
            if (_isDoubleRed((RBNode) n)) {
                result = false;
                break;
            }
        }

        // Check Black depth property
        if (_getBlackHeight((RBNode) this.root) == -1) {
            result = false;
        }

        return result;
    }

    private boolean _isDoubleRed(RBNode node) {
        if (node.colour == RED) {
            if (node.parent != null && ((RBNode) node.parent).colour == RED) {
                return true;
            }
        }
        return false;
    }

    // Returns Black Height
    public int _getBlackHeight(RBNode node) {
        int counter;
        if (node == null) {
            return 0;
        }
        int left = _getBlackHeight((RBNode) node.left);
        int right = _getBlackHeight((RBNode) node.right);
        if (node.colour == BLACK) {
            counter = 1;
        } else {
            counter = 0;
        }

        if (left == -1 || right == -1 || left != right)
            return -1;
        else
            return left + counter;


    }

    // Add helper method.
    protected void _add(Node node, T value) {
        if (value.compareTo(node.value) < 0) {
            if (node.hasLeftChild()) {
                _add(node.left, value);
            } else {
                RBNode newNode = new RBNode((RBNode) node, value);
                // New Nodes are always Red
                newNode.setToRed();
                node.left = newNode;
                // Resolve conflicts
                _rebalanceInsertion(newNode);

            }
        } else {
            if (node.hasRightChild()) {
                _add(node.right, value);
            } else {
                RBNode newNode = new RBNode((RBNode) node, value);
                // New Nodes are always Red
                newNode.setToRed();
                node.right = newNode;
                // Resolve conflicts
                _rebalanceInsertion(newNode);
            }
        }

    }

    private void _rebalanceInsertion(RBNode node) {
        RBNode parent = (RBNode) node.parent;
        if (parent.isRed()) {
            RBNode parentsSibling = (RBNode) parent.getSibling();
            // Case 1. Sibling of parent is black
            if (parentsSibling == null || parentsSibling.isBlack()) {
                // Rotations
                RBNode b  = triNodeRestructure(node);
                b.setToBlack();

                RBNode left = (RBNode) b.left;
                left.setToRed();

                ((RBNode) b.right).setToRed();
            // case 2. Sibling of parent is red
            } else {
                // Recoloring
                ((RBNode) node.parent).setToBlack();
                ((RBNode) node.parent.getSibling()).setToBlack();
                if (!node.getGrandParent().isRoot()) {
                    ((RBNode) node.getGrandParent()).setToRed();
                    // Propogate check
                    _rebalanceInsertion(((RBNode)node.getGrandParent()));
                }

            }
        }

    }

    private RBNode triNodeRestructure(RBNode nodeToRotate) {
        RBNode node = nodeToRotate;
        RBNode parent = (RBNode) nodeToRotate.parent;
        // Single rotation (Nodes in zig)
        if ((node.isLeftChild() && parent.isLeftChild() || (!node.isLeftChild() && !parent.isLeftChild()))) {
            _rotateAboveParent(parent);
            return parent;
        // Double rotation (Nodes in zig zag)
        } else {
            _rotateAboveParent(node);
            _rotateAboveParent(node);
            return node;
        }

    }

}
