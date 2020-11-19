import java.io.FileNotFoundException;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Set;
import java.util.TreeMap;
import java.io.File;
import java.io.PrintWriter;
import java.util.concurrent.CountDownLatch;

class Recipient implements Runnable {
    private Monitor monitor;
    private CountDownLatch readyThreads;
    private CountDownLatch threadBlocker;
    TreeMap<Integer, ArrayList<Message>> messages = new TreeMap<>();

    public Recipient(Monitor newMonitor, CountDownLatch ready, CountDownLatch blocker) {
        this.monitor = newMonitor;
        this.readyThreads = ready;
        this.threadBlocker = blocker;
    }


    public void sortAndPrint() throws FileNotFoundException, UnsupportedEncodingException {

        Set<Integer> keyChannels = this.messages.keySet();
        for (Integer key: keyChannels) {
            //File f = new File(String.format("/Users/yauhenkhutarniuk/Documents/UiO/in1010/oblig_6/src/%d.txt", key));
            File f = new File(String.format("%d.txt", key));
            PrintWriter r = new PrintWriter(f, "utf-8");

            Collections.sort(this.messages.get(key)); //Here we sort
            for (Message msg: this.messages.get(key)) {
                r.print(msg.getMessage() + "\n");
            }

            r.close();
        }


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
                if (!this.monitor.transmissionSwitch && this.monitor.messageQueue.size() == 0){
                    not_ready = false;
                    break;
                }
                // Get message and put it to HashSet with Arrays
                Thread.sleep(500);
                Message nextMessage = this.monitor.getMessage();

                if (nextMessage != null) {
                    if (this.messages.containsKey(nextMessage.getChannelID())) {
                        this.messages.get(nextMessage.getChannelID()).add(nextMessage);
                    } else {
                        ArrayList<Message> m = new ArrayList<>();
                        m.add(nextMessage);
                        this.messages.put(nextMessage.getChannelID(), m);
                    }

                }

            }
            this.sortAndPrint();
        } catch (Exception e) {
            System.out.println("Got exception in Cryptographer");
        }
    }
}
