import java.util.concurrent.CountDownLatch;

public class Cryptographer implements Runnable {
    private final String BEACON = "STOP";
    private Monitor monitorOne;
    private Monitor monitorTwo;
    private CountDownLatch readyThreads;
    private CountDownLatch threadBlocker;

    public Cryptographer(Monitor newMonitorOne, Monitor newMonitorTwo, CountDownLatch ready, CountDownLatch blocker) {
        this.monitorOne = newMonitorOne;
        this.monitorTwo = newMonitorTwo;
        this.readyThreads = ready;
        this.threadBlocker = blocker;
    }

    public void run() {
        // Notify main program that the thread is ready
        this.readyThreads.countDown();
        try {
            // Wait for other threads
            this.threadBlocker.await();
            // RUN
            boolean not_ready = true;
            while(not_ready) {
                if (!this.monitorOne.transmissionSwitch && this.monitorOne.messageQueue.size() == 0) {
                    this.monitorTwo.addMessage(new Message(0, 0, BEACON));
                    not_ready = false;
                    break;
                }

                Message nextMessage = this.monitorOne.getMessage();
                if (nextMessage != null) {
                    String decryptedMessage = Kryptografi.dekrypter(nextMessage.getMessage());
                    nextMessage.setMessage(decryptedMessage);
                    this.monitorTwo.addMessage(nextMessage);
                    //System.out.println(monitorTwo.messageQueue.size());
                }

            }

        } catch (Exception e) {
            System.out.println("Got exception in Cryptographer");
        }
    }
}
