public class Cajero{ 
    private String nombre;
    private Double sueldo;
    private Integer ventas;

    public Cajero(String nombre, Double sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.ventas = 0;
    }

    public void vender(Double monto){
        this.ventas += 1;
        this.sueldo+=  monto*0.6;
    }
    public Integer getVentas(){
        return this.ventas;
    }
    
}