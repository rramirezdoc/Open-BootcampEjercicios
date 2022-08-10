public class App {
    public static void main(String[] args) throws Exception {
        
        Cliente cliente = new Cliente();

        cliente.edad = 42;
        cliente.telefono = "+56 979576085";
        cliente.nombre = "Rodrigo Ramirez";
        cliente.credito = 500000;

        System.out.println("Edad : " + cliente.edad );
        System.out.println("Teléfono : " + cliente.telefono);
        System.out.println("Nombre : " + cliente.nombre);
        System.out.println("Crédito : " + cliente.credito);
    }
}
