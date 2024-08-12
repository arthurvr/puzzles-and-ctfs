'use strict';

import { WriteStream, createWriteStream } from "fs";
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString: string = '';
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on('data', function(inputStdin: string): void {
    inputString += inputStdin;
});

process.stdin.on('end', function(): void {
    inputLines = inputString.split('\n');
    inputString = '';

    main();
});

function readLine(): string {
    return inputLines[currentLine++];
}

/*
 * Complete the 'circularPalindromes' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts STRING s as parameter.
 */

function isPalindrome(str: string): boolean {
    var len = str.length;
    for (var i = 0; i < len/2; i++) {
        if (str[i] !== str[len - 1 - i]) {
            return false;
        }
    }
    return true;
}

function getAllSubstrings(str: string): string[] {
  let result: string[] = [];

  for (let i = 0; i < str.length; i++) {
      for (let j = i + 1; j < str.length + 1; j++) {
          result.push(str.slice(i, j));
      }
  }
  
  return result;
}

function longestPalindrome(str: string): number {
    let longestLength = 0;
    
    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j < str.length + 1; j++) {
            let sub = str.slice(i, j);
            if (isPalindrome(sub) && sub.length > longestLength) {
                longestLength = sub.length;
            }
        }
    }
    
    return longestLength;
}

function circularPalindromes(s: string): number[] {
    // Write your code here
    let result: number[] = [];
    for (let i = 0; i < s.length; i++) {
        let rotationi = s.substring(i, s.length) + s.substring(0, i);
        result.push(longestPalindrome(rotationi));
    }
    return result;
}

function main() {
    const ws: WriteStream = createWriteStream(process.env['OUTPUT_PATH']);

    const n: number = parseInt(readLine().trim(), 10);

    const s: string = readLine();

    const result: number[] = circularPalindromes(s);

    ws.write(result.join('\n') + '\n');

    ws.end();
}
