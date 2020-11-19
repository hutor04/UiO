import java.util.ArrayList;

public interface BSTOper<T> {
    public void add( T value );
    public boolean remove( T value );
    public int size();
    public boolean existsInTree( T value );
    public T findNearestSmallerThan( T value );
    public void addAll( ArrayList<T> integers );
    public ArrayList<T> sortedArray() ; // inorder
    public ArrayList<T> findInRange (T low, T high);
}
