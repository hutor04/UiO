import java.util.ArrayList;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class Monitor {
    // Data
    ArrayList<Message> messageQueue = new ArrayList<>();
    private int noOfChannels;

    // Multi-threading
    private Lock messageQueueLock;
    private Condition emptyMessageQueue;
    private int finishedListeners = 0;

    boolean transmissionSwitch = true;
    private final String BEACON = "STOP";

    // Constructor
    public Monitor(int newNoOfChannels) {
        this.noOfChannels = newNoOfChannels;
        messageQueueLock  = new ReentrantLock();
        emptyMessageQueue = messageQueueLock.newCondition();
    }

    // Add Message
    public void addMessage(Message newMessage) {
        // Lock the shared resource
        messageQueueLock.lock();
        try {
            // Check for STOP beacon.
            if (newMessage.getMessage().equals(BEACON)) {
                finishedListeners++;
                if ((this.noOfChannels == this.finishedListeners)) {
                    transmissionSwitch = false;
                    emptyMessageQueue.signalAll();
                }
            } else {
                messageQueue.add(newMessage);

                // Notify waiters that the queue may be not empty
                emptyMessageQueue.signalAll();
            }
        } finally {
            // Unlock the resource
            messageQueueLock.unlock();
        }

    }

    public Message getMessage() {
        // Lock the shared resource
        messageQueueLock.lock();
        try {
            // Conditional lock, queue is empty
            while (this.messageQueue.size() < 1 && this.transmissionSwitch) {
                emptyMessageQueue.await();
            }
            Message nextMessage = messageQueue.remove(0);
            return nextMessage;

        } catch (Exception e) {
            return null;
        }
        finally {
            // Unlock the resource
            messageQueueLock.unlock();
        }
    }

}
