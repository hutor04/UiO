class Message implements Comparable<Message> {
    private static int totalChannels = 0;
    private static int totalMessages = 0;

    private int channelID;
    private int messageID;
    private String message;

    public Message(int channel, int message, String text) {
        if (channel > totalChannels) {
            totalChannels = channel;
        }

        if (message > totalMessages) {
            totalMessages = message;
        }

        this.channelID = channel;
        this.messageID = message;
        this.message = text;
    }

    @Override
    public int compareTo(Message newObject) {
        return Integer.compare(this.messageID, newObject.getMessageID());
    }

    public int getChannelID() {
        return this.channelID;
    }

    public int getMessageID() {
        return this.messageID;
    }

    public String getMessage() {
        return message;
    }

    public static int getTotalChannels() {
        return totalChannels;
    }

    public static int getTotalMessages() {
        return totalMessages;
    }

    public void setMessage(String newMessage) {
        this.message = newMessage;
    }
}
