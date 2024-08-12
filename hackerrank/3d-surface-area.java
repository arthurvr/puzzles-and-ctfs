import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'surfaceArea' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY A as parameter.
     */

    public static int surfaceArea(List<List<Integer>> A) {
        int result = 0;
        
        int m = A.size();
        int n = A.get(0).size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int x = A.get(i).get(j);
                
                int up = 0;
                int right = 0;
                int down = 0;
                int left = 0;
                
                if (i > 0) {
                    up = A.get(i-1).get(j);
                }
                
                if ( j < n - 1 ) {
                    right = A.get(i).get(j+1);
                }
                
                if (i < m - 1) {
                    down = A.get(i+1).get(j);
                }
                
                if (j > 0) {
                    left = A.get(i).get(j-1);
                }
                
                result += 2;
                
                if (up < x) result += x - up;
                if (right < x) result += x - right;
                if (down < x) result += x - down;
                if (left < x) result += x - left;
            }
        }
        
        return result;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int H = Integer.parseInt(firstMultipleInput[0]);

        int W = Integer.parseInt(firstMultipleInput[1]);

        List<List<Integer>> A = new ArrayList<>();

        IntStream.range(0, H).forEach(i -> {
            try {
                A.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int result = Result.surfaceArea(A);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
