import java.util.ArrayList;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.CountDownLatch;

class TestListener {
    static int channels = 3;
    static int cryptographers = 5;
    static int recipients = 1;

    public static void main(String[] args) throws InterruptedException {
        Operasjonssentral ops = new Operasjonssentral(channels);
        Kanal[] kanaler = ops.hentKanalArray();
        Monitor mon1 = new Monitor(kanaler.length);
        Monitor mon2 = new Monitor(cryptographers);

        // Sync the start of all threads
        CountDownLatch readyThreads = new CountDownLatch(channels + cryptographers + recipients);
        CountDownLatch threadBlocker = new CountDownLatch(1);

        // Create listeners
        List<Thread> listenerL = new ArrayList<>();
        for (Kanal channel: kanaler) {
            listenerL.add(new Thread(new Listener(mon1, channel, readyThreads, threadBlocker)));
        }

        // Create cryptographers
        List<Thread> cryptographerL = new ArrayList<>();
        for (int i = 0; i < cryptographers; i++) {
            cryptographerL.add(new Thread(new Cryptographer(mon1, mon2, readyThreads, threadBlocker)));
        }

        // Create recipients
        List<Thread> recipientsL = new ArrayList<>();
        for (int i = 0; i < recipients; i++) {
            recipientsL.add(new Thread(new Recipient(mon2, readyThreads, threadBlocker)));
        }

        // Start the threads
        listenerL.forEach(Thread::start);
        cryptographerL.forEach(Thread::start);
        recipientsL.forEach(Thread::start);

        // Sync start
        readyThreads.await();

        // Print out status of the system
        System.out.println("Threads are ready! Startting the system...");
        System.out.println(String.format("Number of Listeners: %d", listenerL.size()));
        System.out.println(String.format("Number of Cryptographers: %d", cryptographerL.size()));
        System.out.println(String.format("Number of Recipients: %d", recipientsL.size()));
        threadBlocker.countDown();

        // Check status via scheduled task
        Timer timer = new Timer();
        class ThreadChecker extends TimerTask {
            private Timer t;
            Monitor mon1;
            Monitor mon2;
            private int l = 0;
            private int c = 0;
            private int r = 0;
            public ThreadChecker(Timer newTimer, Monitor m1, Monitor m2) {
                this.t = newTimer;
                this.mon1 = m1;
                this.mon2 = m2;
            }

            @Override
            public void run() {
                int l1 = 0;
                for (Thread t: listenerL) {
                    if (t.getState() == Thread.State.TERMINATED){
                        l1++;
                    }
                }
                l = l1;

                int c1 = 0;
                for (Thread t: cryptographerL) {
                    if (t.getState() == Thread.State.TERMINATED){
                        c1++;
                    }
                }
                c = c1;

                int r1 = 0;
                for (Thread t: recipientsL) {
                    if (t.getState() == Thread.State.TERMINATED){
                        r1++;
                    }
                }
                r = r1;
                if (r == 1) {
                    this.t.cancel();
                    this.t.purge();
                }

                System.out.println(String.format("Messages in Mon1: %d, Mon2: %d", this.mon1.messageQueue.size(), this.mon2.messageQueue.size()));
                System.out.println(String.format("Terminated listeners: %d, cryptographs: %d, recipients: %d", l, c, r));
            }
        }


        // Run scheduled task
        TimerTask threadCheck = new ThreadChecker(timer, mon1, mon2);
        timer.schedule(threadCheck, 1000, 1000);




    }
}