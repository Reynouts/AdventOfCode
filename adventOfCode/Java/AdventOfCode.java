package adventOfCode;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class AdventOfCode {

	public static void main(String[] args) {
		solveDay1();
		solveDay2part1();
		solveDay2part2();
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

}
