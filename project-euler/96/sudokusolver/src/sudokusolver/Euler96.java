package sudokusolver;

import java.io.*;
import java.nio.file.*;

public class Euler96 {
	public static int[][] readGrid(BufferedReader br) throws IOException {
		int grid[][] = {
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 },
			{ 0, 0, 0, 0, 0, 0, 0, 0, 0 }
		};
		
		for (int i = 0; i < 9; i++) {
			String line = br.readLine();
			
			for (int j = 0; j < 9; j++) {
				grid[i][j] = line.charAt(j) - 48;
			}
		}
		
		return grid;
	}
	
	public static void main(String args[]) throws IOException, FileNotFoundException {
		Path p = Paths.get("./src/p096_sudoku.txt");
		int resultSum = 0;
		

		BufferedReader br = Files.newBufferedReader(p);
		String st;
		while ((st = br.readLine()) != null) {
			if (st.startsWith("Grid")) {	        		
				Sudoku s = new Sudoku(readGrid(br));
				s.solve(0, 0);
				resultSum += s.topLeftCornerNumber();
			}
		}
	        
		System.out.println(resultSum);
		br.close();

	}
}
