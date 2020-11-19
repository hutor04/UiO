import java.util.concurrent.CountDownLatch;

class Listener implements Runnable {
    private Monitor monitor;
    private Kanal channel;
    private int channelID;
    private final String BEACON = "STOP";
    private CountDownLatch readyThreads;
    private CountDownLatch threadBlocker;

    public Listener(Monitor newMonitor, Kanal newChannel, CountDownLatch ready, CountDownLatch blocker) {
        this.channel = newChannel;
        channelID = this.channel.hentId();
        this.monitor = newMonitor;
        this.readyThreads = ready;
        this.threadBlocker = blocker;

    }

    // Add channel ID, and message ID, and forward the message
    private void forwardMessage(String newMessage, int newID) {
        Message msg = new Message(this.channelID, newID, newMessage);
        monitor.addMessage(msg);

    }

    public void run() {
        // Notify main program that the thread is ready
        this.readyThreads.countDown();
        try {
            // Wait for other threads
            this.threadBlocker.await();
            // RUN
            int messageID = 0;
            boolean ready = false;
            // Listen till you don't get null response.
            while(!ready) {
                String message = channel.lytt();
                if (message == null) {
                    this.forwardMessage(BEACON, messageID);
                    ready = true;
                    break;
                }
                // Try to push the message to the monitor
                this.forwardMessage(message, messageID);
                messageID++;
            }
        } catch (InterruptedException e) {
            System.out.println(String.format("Get exception in Listener thread %d", this.channelID));
        }

    }

}
