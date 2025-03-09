public class Tienda {
    private String nombre;
    private Integer id;
    private Double ingresos;
    private Cajero cajero;

    public Tienda(String nombre, Integer id, Double ingresos, Cajero cajero) {
        this.nombre = nombre;
        this.id = id;
        this.ingresos = ingresos;
        this.cajero = cajero;
    }
    public void SetNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return this.nombre;
    }
    public Integer calcularVentas(){
        return this.cajero.getVentas();
    }

}
