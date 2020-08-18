# my-google-foobar-solutions

In July 2020, a google search unearthed google's hidden coding challenge for me.

I was able to work through the first 3 levels, but sadly could not complete level 4 within the allotted time. The challenge was a lot of fun, and it was great for sharpening my problem solving and programming skills. Below I have included a short description of each problem I encountered.

## Level 1.1
Given a string of any length, return the maximum number of pieces the string can be cut into, such that each piece has the same characters in the same order, and there is no leftover pieces.

#### Examples: 
"abcabc" returns 2 
"abcde" returns 1
"aaaaa" returns 5

## Level 2.1
Given an integer X find the difference between the number of elements for each of the following patterns:
  Pattern 1: SUM(1,2,4,8,16,...) <= X (double with each step)
  Pattern 2: SUM(1,1,2,3,5,8,...) <= X (fibonacci series)

#### Example:
12 returns COUNT(1,1,2,3,5) - COUNT(1,2,4) = 2

## Level 2.2
Given a src and dest input on an 8X8 chess board, find the shortest path from src to dest using only Knight (chess) moves.

## Level 3.1
Given an unordered list L of integers count the number of "triples" where 3 numbers satisfy the following conditions:
  Where i,j,k are the indices of the 3 numbers from L: i < j < k,
  And Li divides Lj,
  And Lj divides Lk.

#### Examples:
[1,2,3,4] returns 2 ([1,2,3],[1,2,4])
[1,2,2,1,4] returns 5 ([1,2,2],[1,2,4],[1,2,4],[1,1,4],[2,2,4])

## Level 3.2
Given a number of bricks n, determine the number of ways we can build a staircase. In this case a staircase must be a list of numbers that sums to the number of bricks, where no 2 numbers in the list are the same, and the list has at least 2 elements (i.e. [2,2] sums to 4 but is not a valid staircase for 4 bricks).

#### Examples
4 returns 1 ([1,3])
6 returns 3 ([1,5],[1,2,3],[2,4])

## Level 3.3
Given an array where each row represents a state, and the number of times that state has gone to each of the other states, determine the probability of each final state. The answer should be returned in the following form:

If probabilities are:
1/3 , 3/4 , 1/2

Return:
[4,9,6,12]

This has created a common denominator for all probabilities, and listed all numerators followed by the common denominator.
  
