import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TaskScheduler {

    // Vertex class
    public class Task implements Comparable<Task> {
        private String taskName;
        private int earlyStart, earlyFinish, lateStart, lateFinish, timeEstimate, requiredManPower, id;

        //Helper data
        private LinkedList<Task> outgoingVertices = new LinkedList<>();
        private LinkedList<Task> incomingVertices = new LinkedList<>();
        private int tempDegree, topoNumber;
        private int distance = Integer.MAX_VALUE;
        private boolean visited = false;

        public Task(int newId) {
            this.id = newId;

        }

        private int getEarlyStart() {
            return this.earlyStart;
        }

        private int getEarlyFinish() {
            return this.earlyFinish;
        }

        private int getStartSlack() {
            return this.lateStart - this.earlyStart;
        }

        public String isCritical() {
            return (this.earlyFinish == this.lateFinish) ? "Yes" : "No";
        }

        private String getDependencies() {
            StringBuilder s = new StringBuilder();
            for (Task t: this.outgoingVertices) {
                s.append(t.id);
                s.append(", ");

            }
            return (s.length() > 2) ? s.substring(0, s.length()-2) : s.toString();
        }

        public String toString() {
            return String.format("ID: %d Req.Time: %d ES:%d, EF:%d, LS:%d, LF:%d", this.id, this.timeEstimate,
                    this.earlyStart, this.earlyFinish, this.lateStart, this.lateFinish);
        }

        public int compareTo(Task v) {
            return Integer.compare(this.distance, v.distance);
        }


    }

    // Graph class
    private boolean isCyclic;
    private int projectDuration = 0;
    private HashMap<Integer, Task> vertices = new HashMap<>(); // All tasks here
    private int[] topS; // Top sorting

    public TaskScheduler(String fileName) throws FileNotFoundException {

        File file = new File(fileName);
        Scanner scanner = new Scanner(file);
        Pattern pattern = Pattern.compile("(?<id>\\d+)\\s+(?<taskname>[\\w|-]+)\\s+(?<time>\\d+)\\s+(?<power>\\d+)(?<prev>.*)0");
        int size = scanner.nextInt();

        // Initiate Vertices
        for (int i = 1; i < size + 1; i++) {
            this.vertices.put(i, new TaskScheduler.Task(i));
        }

        // Populate with data
        while (scanner.hasNextLine()) {
            String s = scanner.nextLine();
            //System.out.println(s);
            Matcher matcher = pattern.matcher(s);
            if (matcher.matches()) {
                // Task ID
                Task t = this.vertices.get(Integer.parseInt(matcher.group("id")));
                // Task Name
                t.taskName = matcher.group("taskname");
                // Task time estimate
                t.timeEstimate = Integer.parseInt(matcher.group("time"));
                // Task manpower
                t.requiredManPower = Integer.parseInt(matcher.group("power"));
                // Dependencies
                String prev = matcher.group("prev");

                // Scan dependencies
                Scanner scannerPrev = new Scanner(prev);
                while (scannerPrev.hasNextInt()) {
                    int taskID = scannerPrev.nextInt();
                    Task origin = this.vertices.get(taskID);
                    insertEdge(origin, t);
                }
                scannerPrev.close();
            }
        }
        scanner.close();
    }

    public boolean isCyclic() {
        return this.isCyclic;
    }

    private void insertEdge(Task origin, Task destination)  {
        origin.outgoingVertices.add(destination);
        destination.incomingVertices.add(origin);
    }

    public int getProjectDuration() {
        return this.projectDuration;
    }

    public void printSchedule(PrintWriter printFile) {
        ArrayList<Task> tasks = new ArrayList<>(this.vertices.values());
        tasks.sort(Comparator.comparing(Task::getEarlyStart));
        String hdelimiter = "----------------------------------------------------------------------------------------" +
                "-------------------------------------------";
        String header = String.format("%5s | %35s | %11s | %12s | %11s | %12s | %11s | %10s", "ID", "NAME", "EARLY START",
                "EARLY FINISH", "LATE START", "LATE FINISH", "START SLACK", "CRITICAL");

        System.out.println(hdelimiter);
        printFile.println(hdelimiter);

        System.out.println(header);
        printFile.println(header);

        System.out.println(hdelimiter);
        printFile.println(hdelimiter);

        tasks.forEach(x -> {String line = String.format("%5d | %35s | %11d | %12d | %11d | %12s | %11d | %10s", x.id, x.taskName,
                x.earlyStart, x.earlyFinish, x.lateStart, x.lateFinish, x.getStartSlack(), x.isCritical());
                System.out.println(line);
                printFile.println(line);
        });

        System.out.println(hdelimiter);
        printFile.println(hdelimiter);
    }

    public void printTaskInfo(PrintWriter printFile) {
        String hdelimiter = "--------------------------------------------------------------------------" +
                "------------------";

        String header = String.format("%5s | %35s | %11s | %12s | %11s ", "ID", "NAME", "EST. TIME",
                "MAN POWER", "DEPENDENCIES");

        System.out.println(hdelimiter);
        printFile.println(hdelimiter);

        System.out.println(header);
        printFile.println(header);

        System.out.println(hdelimiter);
        printFile.println(hdelimiter);

        for (int i = 1; i <= this.vertices.size(); i++) {
            Task task = this.vertices.get(i);
            String line = String.format("%5d | %35s | %11d | %12d | %11s", task.id, task.taskName,
                    task.timeEstimate, task.requiredManPower, task.getDependencies());
            System.out.println(line);
            printFile.println(line);

        }

        System.out.println(hdelimiter);
        printFile.println(hdelimiter);
    }

    public void printEmulation(PrintWriter filePrinter) {
        PriorityQueue<Task> upComingTasks = new PriorityQueue<>(Comparator.comparing(Task::getEarlyStart));
        PriorityQueue<Task> inProgress = new PriorityQueue<>(Comparator.comparing(Task::getEarlyFinish));

        upComingTasks.addAll(this.vertices.values());

        int timeStamp;
        int workForce = 0;
        boolean updated;

        String hdelimiter = "-------------------------------------------------------";
        String header = String.format("%5s | %10s | %12s | %12s", "TIME", "STAFF", "TASKS STARTED",
                "TASK ENDED");

        System.out.println(hdelimiter);
        System.out.println(header);
        System.out.println(hdelimiter);

        filePrinter.println(hdelimiter);
        filePrinter.println(header);
        filePrinter.println(hdelimiter);

        for (int i = 0; i <= this.projectDuration; i++) {
            timeStamp = i;
            updated = false;
            StringBuilder startedTask = new StringBuilder("");
            StringBuilder endedTask = new StringBuilder("");

            while(!upComingTasks.isEmpty() && upComingTasks.peek().earlyStart == i) {
                updated = true;
                Task newTask = upComingTasks.poll();
                workForce += newTask.requiredManPower;
                startedTask.append(String.format("%d, ", newTask.id));
                inProgress.add(newTask);
            }

            while(!inProgress.isEmpty() && inProgress.peek().earlyFinish == i) {
                updated = true;
                Task finishedTask = inProgress.poll();
                workForce -= finishedTask.requiredManPower;
                endedTask.append(String.format("%d, ", finishedTask.id));
            }

            if (updated) {
                String s = (startedTask.length() > 2) ? startedTask.substring(0, startedTask.length() - 2) : startedTask.toString();
                String e = (endedTask.length() > 2) ? endedTask.substring(0, endedTask.length() - 2) : endedTask.toString();
                String r = String.format("%5d | %10d | %12s | %12s", timeStamp, workForce, s, e);
                System.out.println(r);
                filePrinter.println(r);
            }

        }
        System.out.println(hdelimiter);
        filePrinter.println(hdelimiter);


    }

    // >>> MAIN ALGORITHM <<<
    // DAG Shortest path
    public void getEstimates() {
        _topsort();
        if (!this.isCyclic) {
            _relaxBackward();
        }
    }

    private void _topsort() {
        this.isCyclic = false;
        this.topS = new int[this.vertices.size()]; // Initiate array
        LinkedList<Task> queue = new LinkedList<>();

        int counter = 0;

        for (Task vertex : this.vertices.values()) { // Initiate start/finish values and populate the queue
            vertex.tempDegree = vertex.incomingVertices.size();
            if (vertex.incomingVertices.size() == 0) {
                queue.add(vertex);
                vertex.earlyStart = 0;
                vertex.earlyFinish = vertex.earlyStart + vertex.timeEstimate;
                vertex.lateFinish = Integer.MAX_VALUE;
            } else {
                vertex.earlyStart = Integer.MIN_VALUE;
                vertex.lateFinish = Integer.MAX_VALUE;
            }
        }
        while (!queue.isEmpty()) {
            Task vertex = queue.poll();
            this.topS[counter] = vertex.id; // Store reference to id.
            vertex.topoNumber = ++counter;
            _relaxForward(vertex); // Edge "relaxation" inverted.

            for (Task v : vertex.outgoingVertices) {
                v.tempDegree = v.tempDegree - 1;
                if (v.tempDegree == 0) {
                    queue.add(v);
                }
            }

        }

        if (counter != this.vertices.size()) {
            this.isCyclic = true;
        }

    }

    // Edge "relaxation"
    private void _relaxForward(Task task) {
        for (Task v: task.outgoingVertices) {
            if (task.earlyFinish > v.earlyStart) {
                v.earlyStart = task.earlyFinish;
                v.earlyFinish = v.earlyStart + v.timeEstimate;
                if (v.earlyFinish > this.projectDuration) {
                    this.projectDuration = v.earlyFinish; // Update Project finish
                }
            }
        }
    }

    // Edge "relaxation"
    private void _relaxBackward() {
        for (int i = this.topS.length - 1; i >= 0; i--) {
            Task task = this.vertices.get(this.topS[i]);
            if (task.outgoingVertices.size() != 0) {
                for (Task v: task.outgoingVertices) {
                    if (task.lateFinish > v.lateStart) {
                        task.lateFinish = v.lateStart;
                        task.lateStart = task.lateFinish - task.timeEstimate;
                    }
                }
            } else {
                task.lateFinish = this.projectDuration;
                task.lateStart = task.lateFinish - task.timeEstimate;
            }
        }

    }


    public String hasCycles() {
        this.isCyclic = false;

        ArrayList<Task> cycle = new ArrayList<>();
        Set<Task> stack = new HashSet<>();
        String result = "";

        if (this.vertices.size() > 0) {
            this.isCyclic = _detectCyclesDirected(this.vertices.get(1), stack, cycle);
            }

        StringBuilder temp = new StringBuilder();
        cycle.forEach(x -> temp.append(x.id + ", "));
        if (temp.length() > 2) {
            result = "Cycle IDs: " + temp.toString().substring(0, temp.length() - 2);
        }

        return result;

    }

    private boolean _detectCyclesDirected(Task seed, Set<Task> stack, ArrayList<Task> cyc) {
        if (stack.contains(seed)) { // Check if node is in current recursion stack
            return true;
        }
        if (seed.visited) {
            return false;
        }
        seed.visited = true; // Set start node as visited
        stack.add(seed); // Add start node to current stack
        for (Task vertex: seed.outgoingVertices) {
            if (_detectCyclesDirected(vertex, stack, cyc)) { // If neighbour is not visited recursively go down there
                if (!cyc.contains(vertex)) {
                    cyc.add(vertex);
                }
                return true;
            }
        }
        stack.remove(seed);
        return false;
    }
}

class Oblig2 {
    public static void main(String[] args) throws FileNotFoundException {
        TaskScheduler t;

        if (args.length > 0) {
            t = new TaskScheduler(args[0]);
        } else {
            t = new TaskScheduler("examplefigure.txt");
        }

        PrintWriter printFile = new PrintWriter("output.txt");
        String cycles = t.hasCycles();
        String realizable = (t.isCyclic()) ? String.format("No\n%s", cycles) : "Yes";
        System.out.println(String.format(">>> Is the project realizable: %s", realizable));
        printFile.println(String.format(">>> Is the project realizable: %s", realizable));
        if (t.isCyclic()) {
            printFile.close();
        } else {
            t.getEstimates();
            System.out.println(String.format(">>> Running time (optimal): %d units.", t.getProjectDuration()));
            printFile.println(String.format(">>> Running time (optimal): %d units.", t.getProjectDuration()));
            System.out.println(">>> Tasks Info:");
            printFile.println(">>> Tasks Info:");
            t.printTaskInfo(printFile);
            System.out.println(">>> Optimal schedule:");
            printFile.println(">>> Optimal schedule:");
            t.printSchedule(printFile);
            printFile.println(">>> Execution emulation:");
            System.out.println(">>> Execution emulation:");
            t.printEmulation(printFile);
            printFile.close();
        }

    }
}
