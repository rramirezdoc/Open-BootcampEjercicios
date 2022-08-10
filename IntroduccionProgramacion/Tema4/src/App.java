public class App {
    public static void main(String[] args) throws Exception {
        //Parte 1//
        System.out.println("-----Parte 1-----");
        int numeroIf;
        numeroIf = -10;

        if (numeroIf > 0){
            System.out.println("numeroIf es MAYOR a 0");
        } else if(numeroIf == 0){
            System.out.println("numeroIf es IGUAL a 0");
        }else{
            System.out.println("numeroIf es MENOR a 0");
        }

        //Parte 2//
        System.out.println("-----Parte 2-----");
        int numeroWhile;
        numeroWhile = -1;

        while(numeroWhile < 3){
            System.out.println("numeroWhile : " + numeroWhile);

            numeroWhile++;
        }

        //Parte 3//
        System.out.println("-----Parte 3-----");
        int numeroDoWhile;
        numeroDoWhile = 2;

        do {
            System.out.println("numeroDoWhile : " + numeroDoWhile);
            numeroDoWhile++;
        } while (numeroDoWhile < 3);
            
        //Parte 4//  
        System.out.println("-----Parte 4-----"); 
        for (int numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println("numeroFor : " + numeroFor);
        }

        //Parte 5//  
        System.out.println("-----Parte 5-----");
        String estacion;
        estacion = "primavera";

        switch (estacion) {
            case "verano":
                System.out.println("Estacion verano");
                break;
            case "primavera":
                System.out.println("Estacion primavera");
                break;
            case "otoño":
                System.out.println("Estacion otoño");
                break;
            case "invierno":
                System.out.println("Estacion invierno");
                break;        
            default:
                System.out.println("No es una estación del año");
                break;
        }
    }
}
