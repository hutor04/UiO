class Stabel<T> extends Lenkeliste<T> {

    /**
     * Inserts a new element to the end of the list.
     * @param x Object of any type.
     */
    public void leggPaa (T x) {
        super.leggTil(x);
    }

    /**
     * Deletes the last element in the list and returns it.
     * @return the last element in the list.
     */
    public T taAv() {
        return super.fjern(super.stoerrelse() - 1);
    }
}
