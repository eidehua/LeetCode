/*

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order.


Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
*/
public class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return new int[0];
        }
        
        int M = matrix.length;
        int N = matrix[0].length;
        
        int[] out = new int[M*N]; //if m = n = 3. and matrix[1,0] = 4, out[1*3 + 0 = 3] = 4
        // so formula is out[row*M + col]
        
        int currRow = 0;
        int currCol = 0;
        // going up diagonal, aka from [2,0] -> [1,1] (decrease row, increase column)
        // going down diagonal, aka from [0,1] -> [1,0] (increase row, decrease column)
        boolean direction_is_up = true;
        
        int index = 0;
        while(true) {
            //System.out.println(currRow + "," + currCol);
            out[index++] = matrix[currRow][currCol];
            // at last element! woo!
            if (currRow == M - 1 && currCol == N - 1) {
                return out;
            }
            int nextRow;
            int nextCol;
            if (direction_is_up) {
                nextRow = currRow-1;
                nextCol = currCol+1;
            } else {
                nextRow = currRow+1;
                nextCol = currCol-1;
            }
            // so we can't go along the same diagonal direction anymore!!!
            if (nextRow < 0 || nextRow >= M || nextCol < 0 || nextCol >= N) {
                //if i was up direction before, I start with either element to right, if i can't have that, to down
                if(direction_is_up) {
                    if (nextCol < N) {
                        nextRow = currRow; // take right element
                    } else {
                        nextCol = currCol; // take down element
                        nextRow = currRow + 1;
                    }
                    direction_is_up = false;
                } else {
                    if (nextRow < M) {
                        nextCol = currCol; // take down element
                    } else {
                        nextRow = currRow; // take right element
                        nextCol = currCol+1;
                    }
                    direction_is_up = true;
                }
                // if I was down direction before, I start with either down element, or right element
            }
            
            currRow = nextRow;
            currCol = nextCol;
        }
    }
}
/*
3x3: 1,2,3,2,1
2x2: 1,2,1
4x4: 1,2,3,4,3,2,1

pattern: go up, then down, then up, etc...
but it is M x N


[
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9,10,11,12 ],
 [13,14,15,16 ]
]

4 x 3: 1,2,3,3,2,1
[
 [ 1, 2, 3 ],
 [ 5, 6, 7 ],
 [ 9,10,11 ],
 [13,14,15 ]
]
[1,2,5,9,6,3,7,10,13,14,11,15]

start: 0,0 end: 0,0
start: 0,1 end: 1,0
start: 2,0 end: 0,3

*/