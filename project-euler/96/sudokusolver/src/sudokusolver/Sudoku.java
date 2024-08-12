package sudokusolver;

public class Sudoku {
	int grid[][];
	
	public Sudoku(int[][] grid) {
		super();
		
		this.grid = grid;
	}

	public int topLeftCornerNumber() {
		return grid[0][0]*100 + grid[0][1]*10 + grid[0][2];
	}
	
	public void print() {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				System.out.print(grid[i][j] + " ");
			}
			
			System.out.println();
		}
	}
	
	public boolean isSafe(int row, int col, int num) {
		for (int x = 0; x <= 8; x++) {
			if (grid[row][x] == num) {
				return false;
			}		
		}
		
		for (int x = 0; x <= 8; x++) {
			if (grid[x][col] == num) {
				return false;
			}
		}
		
		int startRow = row - row % 3;
		int startCol = col - col % 3;
		
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (grid[i + startRow][j + startCol] == num) {
					return false;
				}		
			}		
		}
	
		return true;
	}
	
	public boolean solve(int row, int col) {
		if (row == 8 && col == 9) {
			return true;
		}
		
		if (col == 9) {
			row++;
			col = 0;
		}
		
		if (grid[row][col] != 0) {
			return solve(row, col + 1);
		}
		
		for (int num = 1; num < 10; num++) {
			if (isSafe(row, col, num)) {
				grid[row][col] = num;
				if (solve(row, col + 1)) {
					return true;
				}
			}
			
			grid[row][col] = 0;
		}
		
		return false;
	}
}

