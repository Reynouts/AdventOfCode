
public class Day15 {

    public static void main(String[] args)  {
    	long startTime = System.nanoTime();      
    	
    	long genA = 116;
        long genB = 299;
        //System.out.println("part 1 " + generator(genA, genB, 40000000, false)); 
        System.out.println("part 2 " + generator(genA, genB, 5000000, true));

        long difference = System.nanoTime() - startTime;
        System.out.println("Elapsed time in seconds: " + difference / 1000000000.0);

    }       

    

    public static long getNextGenerator(long generator, boolean picky, int modulo, int multiplier) {
        generator = (generator * multiplier) % 2147483647;
        if (picky) {
        	while(generator % modulo != 0) {
                generator = (generator * multiplier) % 2147483647;
        	}
        }
        return generator;
    }
    
    public static int generator(long genA, long genB, int cycles, boolean picky) {
        int count = 0;
        for (int i = 0; i < cycles; i++) {
        	genA = getNextGenerator(genA, picky, 4, 16807);
            genB = getNextGenerator(genB, picky, 8, 48271);
            if ((genA & 65535) == (genB & 65535))
                count++;
        }
        return count;    	
    }

}