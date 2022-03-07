class Animal {
    public void status() {
        System.out.println("An animal runs on the street.");
    }
}
class Vehicle {
    public void status() {
        System.out.println("A vehicle drives on the street.");
    }
}
public class street {
    public static void in_the_street(Object obj) {
        if (obj instanceof Animal)
            ((Animal) obj).status();
        if (obj instanceof Vehicle)
            ((Vehicle) obj).status();
    }
    public static void main(String[] args) {
        Animal dog = new Animal();
        Vehicle car = new Vehicle();
        in_the_street(dog);
        in_the_street(car);
    }
}
