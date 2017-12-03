package adventOfCode;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.function.BiFunction;
import java.util.function.Function;

public class AdventOfCode {

	public static void main(String[] args) {
		solveDay1();
		solveDay2part1();
		solveDay2part2();
		solveDay3(289326, true); //my number is 289326

	}
	
	//////////////////////////
	// DAY 1 --- 01-12-2017 //
	//////////////////////////
	public static void solveDay1 () {
		// Day 1: Inverse Captcha
		String input = readFileSafe("Day1.txt");
		
		int total = 0;
		int shift = input.length() / 2; // for first puzzle, shift is 1

		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) == input.charAt((i + shift) % input.length())) {
				total += Character.getNumericValue(input.charAt(i));
			}
		}
		System.out.println("Day 1\n Total Number for the inverse captcha: " + total);		
	}
	
	//////////////////////////
	// DAY 2 --- 02-12-2017 //
	//////////////////////////
	public static void solveDay2part1() {
		// Part 1: look for highest-lowest in row and checksum
		String input = readFileSafe("Day2.txt");	
		String lines[] = input.split("\\r?\\n");
		int sum = 0;
		for (String line : lines) {
			String elements[] = line.split("\\t");
			int lowest = Integer.MAX_VALUE;
			int highest = 0;
			for(String element: elements) {
				int number = Integer.parseInt(element);
				if (number < lowest) {
					lowest = number;
				}
				if (number > highest) {
					highest = number;
				}
			}
			sum += (highest - lowest);
		}
		System.out.println("Day 2.1\n Checksum highest-lowest: " + sum);
	}
	
	public static void solveDay2part2() {
		//Part 2: check for evenly divisible values per row and checksum 
		String input = readFileSafe("Day2.txt");	
		String lines[] = input.split("\\r?\\n");
		int sum = 0;
		for (String line : lines) {
			String elements[] = line.split("\\t");
			for(String element: elements) {
				int number = Integer.parseInt(element);
				for(String element2: elements) {
					if(element2 != element) {
						int number2 = Integer.parseInt(element2);
						if (number%number2 == 0) {
							sum += (number/number2);
							break;
						}	
					}
				}
			}
		}
		System.out.println("Day 2.2\n Checksum evenly divisible values: " + sum);
	}
	
	//////////////////////////
	// DAY 3 --- 03-12-2017 //
	//////////////////////////
	public static void solveDay3(int number, boolean surrounding) {	
		//Generate grid, when surrounding needs to be calculated, we don't know how big the array needs to be..
		int width = 0;
		if(!surrounding) {
			width = calculateWidthForGrid(number);
		}
		else {
			width = 11; //fits for my number, but to be safe: make it larger
		}
		
		//initialize starting point of grid
		int[][] grid = new int[width][width];
		int middle = (width/2);
		
		grid[middle][middle] = 1;
		
		int x = middle;
		int y = middle;
		
		//walk around the filled grid until the number is in the filled grid
		while(fillGridAround(grid, x, y, surrounding) < number) {
			x++;
			y++;
		}
		
		//find target position and which number is the first number that is bigger than target
		int targetX = 0;
		int targetY = 0;
		int lowest = Integer.MAX_VALUE;
		for(int i = 0; i < grid.length; i++)
		{
		    for(int j = 0; j < grid[i].length; j++)
		    {
		        if(grid[j][i] == number) {
		        	targetX = j;
		        	targetY = i;
		        }
		        if(grid[j][i] > number && grid[j][i] < lowest) {
		        	lowest = grid[j][i];
		        }
		    }
		}		

		//calculate manhattan distance and print solution
		int distance = Math.abs(targetX-middle) + Math.abs(targetY-middle);
		System.out.println("Day 3.1");
		System.out.println(" Distance to goal: " + distance);
		System.out.println("Day 3.2");
		System.out.println(" First element bigger than target: " + lowest);
	}
	
	public static int fillGridAround(int[][] grid, int x, int y, boolean surrounding) {
		//walk around the (until now) filled grid, and fill the squares with numbers.
		//when surrounding is false: just increase number to fill in with 1
		//when surrounding is false: calculate surrounding of square and fill
		// TODO: think of something smart to avoid duplicate code (BiFunction?)
		int number = grid[x][y];
		// step to the right
		x++;
		// step up
		while(grid[x-1][y] != 0) {
			if(surrounding) {
				number = calculateSurrounding(grid, x, y);
			}
			else {
				number++;
			}
			grid[x][y] = number;
			y--;
		}
		// step left
		while(grid[x][y+1] != 0) {
			if(surrounding) {
				number = calculateSurrounding(grid, x, y);
			}
			else {
				number++;
			}			grid[x][y] = number;
			x--;
		}
		// step down
		while(grid[x+1][y] != 0) {
			if(surrounding) {
				number = calculateSurrounding(grid, x, y);
			}
			else {
				number++;
			}			grid[x][y] = number;
			y++;
		}
		// step right
		while(grid[x][y-1] != 0) {
			if(surrounding) {
				number = calculateSurrounding(grid, x, y);
			}
			else {
				number++;
			}			grid[x][y] = number;
			x++;
		}
		
		return number;
	}
	
	public static int calculateWidthForGrid(int number) {
		//when walking around the square and increasing the square with 1, there is a pattern.
		//every right/down corner is a uneven quadratic number (1, 9, 25, 49, ..) -> sqrt = (1, 3, 5, 7, ...)
		//so we can know how big the square needs to be for a arbitrary number
		
		int square = (int) Math.sqrt(number);
		int width = 0;
		
		//number is no nice square
		if(number%square != 0) {
			width = square + 1;
			// uneven
			if(width%2 == 0) {
				width++;
			}
		}
		else {
			width = square;
			if(width%2 == 0) {
				width++;
			}
		}
		
		return width + 2; //margin to make other function easier (no need to check for boundaries)
	}
	
	public static int calculateSurrounding(int[][] array, int x, int y) {
		//calculate sum of all surrounding squares for a target square array[x,y]
		int sum = 0;
		
		if(y+1 < array.length) {
			sum += array[x][y+1];
			if(x+1 < array[0].length) {
				sum += array[x+1][y+1];
			}
			if(x-1 >= 0) {
				sum += array[x-1][y+1];
			}
		}
		if(x+1 < array[0].length) {
			sum += array[x+1][y];

		}
		if(y-1 >= 0) {
			sum += array[x][y-1];
			if(x-1 >= 0) {
				sum += array[x-1][y-1];
			}
			if(x+1 < array[0].length) {
				sum += array[x+1][y-1];
			}
		}
		if(x-1 >= 0) {
			sum += array[x-1][y];
		}

		if (sum == 0){
			sum++;
		}
		return sum;
	}
	
	////////////////////////////////////
	// Some crappy helper functions.. //
	////////////////////////////////////
	public static String readFileSafe(String fileName) {
		try {
			return (readFile(fileName));
		} catch (IOException e) {
			System.out.println("Something went wrong reading the file..");
			return "";
		}
	}

	public static String readFile(String path) throws IOException {
		Charset encoding = StandardCharsets.UTF_8;
		byte[] encoded = Files.readAllBytes(Paths.get(path));
		return new String(encoded, encoding);
	}
	
	public static void printArray(int[][] array) {
		for(int i = 0; i < array.length; i++)
		{
		    for(int j = 0; j < array[i].length; j++)
		    {
		        System.out.print(String.format("%1$9s", array[j][i]));
		        if(j < array[i].length - 1) System.out.print(" ");
		    }
		    System.out.println();
		}
	}

}
