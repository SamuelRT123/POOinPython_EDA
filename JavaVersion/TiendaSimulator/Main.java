public class Main {
    public static void main(String[] args) {
        System.out.println("Bienvenido a la tienda");
        Cajero cajero = new Cajero("Juan", 1000.0);
        cajero.vender(100.0);
        System.out.println("Ventas del cajero " + cajero.getVentas());
        Tienda tienda = new Tienda("Tienda", 1, 0.0, cajero);
        System.out.println("Nombre de la tienda " + tienda.getNombre());


    }
}
