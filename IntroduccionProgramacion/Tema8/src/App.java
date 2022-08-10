public class App {
    public static void main(String[] args) throws Exception {
        Persona persona = new Persona();

        persona.setEdad(41);
        persona.setNombre("Rodrigo Ramirez");
        persona.setTelefono("+56979576085");

        System.out.println("Edad : " + persona.getEdad());
        System.out.println("Nombre : " + persona.getNombre());
        System.out.println("Teléfono : " + persona.getTelefono());
    }
}