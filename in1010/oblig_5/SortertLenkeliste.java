class SortertLenkeliste<T extends Comparable<T>> extends Lenkeliste<T> {

    /**
     * Inserts a new element to the list in the sorted order.
     * @param x Object of any type.
     */
    @Override
    public void leggTil(T x) {
        Node newNode = new Node(x);
        Node beforeCurrent = super.head.getNext();

        while (beforeCurrent != super.tail) {
            if (newNode.getItem().compareTo(beforeCurrent.getItem()) < 0) {
                break;
            } else {
                beforeCurrent = beforeCurrent.getNext();
            }
        }

        newNode.setNext(beforeCurrent);
        newNode.setPrevious(beforeCurrent.getPrevious());

        beforeCurrent.getPrevious().setNext(newNode);
        beforeCurrent.setPrevious(newNode);

        size++;
    }

    /**
     * Deletes the last element in the list and returns it.
     * @return the last element in the list.
     */
    @Override
    public T fjern() {
        return super.fjern(super.stoerrelse() - 1);
    }

    /**
     * Not Implemented
     * @param pos
     * @param x
     */
    @Override
    public void sett(int pos, T x) {
        throw new UnsupportedOperationException();
    }

    /**
     * Not implemented
     * @param pos
     * @param x
     */
    @Override
    public void leggTil(int pos, T x) {
        throw new UnsupportedOperationException();
    }
}
