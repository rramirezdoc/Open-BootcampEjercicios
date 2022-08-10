public class App {
    public static void main(String[] args) throws Exception {
        int n1,n2, n3;
        int resultado;

        n1=2;
        n2=3;
        n3=4;

        resultado = suma(n1, n2, n3);

        System.out.println("suma : " + resultado);

        Coche miCoche =  new Coche();
        miCoche.AgregarPuerta();

        System.out.println("puertas : " + miCoche.puertas);

    }

    public static int suma(int a, int b, int c) {
        return a + b + c;        
    }
}