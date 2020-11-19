import java.util.Iterator;
import java.util.NoSuchElementException;

class Lenkeliste<T> implements Liste<T> {
    protected Node head;
    protected Node tail;
    protected int size;

    public Lenkeliste() {
        this.head = new Node(null);
        this.tail = new Node(null);
        this.head.setPrevious(null);
        this.head.setNext(tail);
        this.tail.setPrevious(head);
        this.tail.setNext(null);
        this.size = 0;
    }

    /**
     * Returns the number of elements in the list.
     * @return An integer representing the number of items in the list.
     */
    @Override
    public int stoerrelse() {
        return this.size;
    }

    /**
     * Inserts an element at the requested position.
     * @param pos Integer between 0 and the size of the list.
     * @param x The element to be inserted.
     */
    @Override
    public void leggTil(int pos, T x) {
        Node newNode = new Node(x);
        if (pos >= 0 && pos <= this.size) {

            Node toMoveNode = this.head.getNext();
            for (int i = 0; i < pos; i++) {
                toMoveNode = toMoveNode.getNext();
            }
            toMoveNode.getPrevious().setNext(newNode);
            newNode.setPrevious(toMoveNode.getPrevious());

            newNode.setNext(toMoveNode);
            toMoveNode.setPrevious(newNode);

            this.size++;

        } else {
            throw new UgyldigListeIndeks(pos);
        }

    }

    /**
     * Inserts a new element to the end of the list.
     * @param x Object of any type.
     */
    @Override
    public void leggTil(T x) {
        Node newNode = new Node(x);

        Node lastButOne = this.tail.getPrevious();

        newNode.setNext(this.tail);
        this.tail.setPrevious(newNode);

        lastButOne.setNext(newNode);
        newNode.setPrevious(lastButOne);

        size++;
    }

    /**
     * Replaces the content an element at the requested position.
     * @param pos Integer between 0 and the size of the list.
     * @param x The element to be inserted.
     */
    @Override
    public void sett(int pos, T x) {
        this.locateNode(pos).setItem(x);
    }

    /**
     * Returns the contents of the element at the required position.
     * @param pos Integer between 0 and the size of the list.
     * @return The contents of the element at the requested position.
     */
    @Override
    public T hent(int pos) {
        return this.locateNode(pos).getItem();
    }

    /**
     * Deletes the element at the required position and returns it.
     * @param pos Integer between 0 and the size of the list.
     * @return The element at the requested position.
     */
    @Override
    public T fjern(int pos) {
        Node toRemoveNode = this.locateNode(pos);
        Node beforeNode = toRemoveNode.getPrevious();
        Node afterNode = toRemoveNode.getNext();

        beforeNode.setNext(afterNode);
        afterNode.setPrevious(beforeNode);

        size--;

        return toRemoveNode.getItem();
    }

    /**
     * Deletes the last element in the list and returns it.
     * @return the last element in the list.
     */
    @Override
    public T fjern() {
        if (this.size > 0) {
            Node toRemoveNode = this.head.getNext();

            this.head.setNext(toRemoveNode.getNext());
            toRemoveNode.getNext().setPrevious(this.head);

            size--;
            return toRemoveNode.getItem();
        } else {
            throw new UgyldigListeIndeks(-1);
        }

    }

    /**
     * Helper method.
     * @param pos Integer between 0 and the size of the list
     * @return Node in the requested position.
     */
    private Node locateNode(int pos) {
        if (this.size > 0 && pos >= 0 && pos < this.size ) {
            Node locatedNode = this.head.getNext();
            for (int i = 0; i < pos; i++) {
                locatedNode = locatedNode.getNext();
            }
            return locatedNode;
        } else {
            if (this.size > 0) {
                throw new UgyldigListeIndeks(pos);
            } else {
                throw new UgyldigListeIndeks(-1);
            }
        }
    }

    public Node getHead() {
        return this.head;
    }

    /**
     * Prints the content of the Lenkeliste in [ item0, item1, ...] format
     * @return [ item0, item1, ...]
     */
    @Override
    public String toString() {
        if (this.stoerrelse() == 0) {
            return "[]";
        } else {
            String result = "[";
            for (T s : this) {
                result += s + ", ";
            }
            return result.substring(0, result.length() - 2) + "]";
        }
    }

    /**
     * Iterator method.
     * @return Return an instance of LenkelisteIterator class.
     */
    @Override
    public Iterator<T> iterator() {
        return new LenkelisteIterator();
    }


    /**
     * Iterator for the Lenkeliste class
     */
    class LenkelisteIterator implements Iterator<T> {
        int current = 0;

        @Override
        public boolean hasNext() {
            return (current < Lenkeliste.this.stoerrelse());
        }

        @Override
        public T next() {
            if (!this.hasNext()) {
                throw new NoSuchElementException();
            } else {
                Node locatedNode = Lenkeliste.this.head.getNext();
                for (int i = 0; i < current; i++) {
                    locatedNode = locatedNode.getNext();
                }
                this.current++;

                return locatedNode.getItem();
            }
        }
    }


    protected class Node {
        protected Node next;
        protected Node previous;
        protected T item;

        public Node(T newItem) {
            this.item = newItem;
        }

        public T getItem() {
            return this.item;
        }

        public void setItem(T newItem) {
            this.item = newItem;
        }

        public Node getNext() {
            return this.next;
        }

        public void setNext(Node nextNode) {
            this.next = nextNode;
        }

        public Node getPrevious() {
            return this.previous;
        }

        public void setPrevious(Node previousNode) {
            this.previous = previousNode;
        }

    }

}