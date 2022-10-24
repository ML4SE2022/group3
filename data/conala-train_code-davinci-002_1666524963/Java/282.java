public class Main {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Hello from thread 1");
            }
        });
        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("Hello from thread 2");
            }
        });
        thread1.start();
        thread2.start();
    }
}