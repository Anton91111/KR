import java.util.PriorityQueue;

public class Main {
    private String toyId;
    private String toyName;
    private int toyWeight;

    public Main(String toyId, String toyName, int toyWeight) {
        this.toyId = toyId;
        this.toyName = toyName;
        this.toyWeight = toyWeight;
    }

    public String getToyId() {
        return toyId;
    }

    public String getToyName() {
        return toyName;
    }

    public int getToyWeight() {
        return toyWeight;
    }

    public static void main(String[] args) {
        // Создаем коллекцию PriorityQueue для хранения игрушек
        PriorityQueue<Main> toyQueue = new PriorityQueue<>((a, b) -> Integer.compare(b.getToyWeight(), a.getToyWeight()));

        // Добавляем игрушки в коллекцию
        toyQueue.add(new Main("1", "Машинка", 10));
        toyQueue.add(new Main("2", "Солдатик", 5));
        toyQueue.add(new Main("3", "Мягкая игрушка", 15));
        toyQueue.add(new Main("4", "Юла", 20));
        toyQueue.add(new Main("5", "Ракета", 3));
        // Вызываем Get 10 раз и записываем результат в файл
        for (int i = 0; i < 10; i++) {
            Main toy = toyQueue.poll();
            if (toy != null) {
                System.out.println("Выпала игрушка: " + toy.getToyName());
            } else {
                System.out.println("Коллекция игрушек пуста.");
            }
        }
    }
}