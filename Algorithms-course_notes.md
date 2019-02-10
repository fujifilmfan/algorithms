Divide and Conquer, Sorting and Searching, and Randomized Algorithms, Stanford University (via Coursera)
========================================================================================================

I. Introduction
---------------

### Video: Integer Multiplication
* an algorithm transforms **input** into desired **output**
* we'll assess the mulitplication algorithm on the basis of the basic number of operations it performs
* can we do better?

### Video: Karatsuba Multiplication

### Video: Merge Sort: Motivation and Example  
Why study this algorithm?  
* perhaps the most transparent application of the Divide-and-Conquer paradigm  
   * divide & conquer improves over selection, insertion, bubble sort (these scale as N^2)  
   * asymptotic analysis focuses on rate of growth on an algorithm's performance  
Background research:   
* I looked up merge sorting in *Algorithms* and ended up reading about primality testing (pp.32-33)  
* which led me to better understand modular arithmetic: https://en.wikipedia.org/wiki/Modular_arithmetic  
* and Fermat's little theorem: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem  
* I'll need to have a better grasp of writing recursive functions:  
   * https://www.youtube.com/watch?v=eqQQoIAT9So  
   * https://www.youtube.com/watch?v=urF1XreNtXI  
   * https://www.youtube.com/watch?v=wMNrSM5RFMc  

### Video: Merge Sort: Pseudocode
* think of running time as the number of operations, like stepping through code in a debugger, about number of lines of code executed  
* running time of merge is <= 4m + 2 (4 for for loop (k incrementing, i,j incrementing, comparisons), 2 for initialization)
   * can be simplified (approximated further) to <= 6m b/c m >= 1
   * I would expect just 4m as m gets large, but better to overestimate?
* log base n (x) == number of times you have to divide x by n to get less than 1

### Video: Merge Sort: Analysis
* prove with recursion tree method
* "So in other words, the number of levels of recursion is exactly the number of
times you need to divide n by 2, until you get down to a number that's most one.
And recall, that's exactly the definition of a logarithm base 2 of n."
* per level <= 2^j x 6(n/2^j) = 6n per level (one thing is doubling while the other halving)
* number of levels = logbase2(n) + 1
* total <= 6n x (logbase2(n) + 1) = 6n x logbase2(n) + 6n

### Video: Guiding Principles for Analysis of Algorithms
* Guiding Principle #1: worst-case analysis
   * appropriate for "general-purpose" routines
   * mathematically simpler
   * could have done
      * "average-case" analysis
      * benchmarks
      * these require domain knowledge, like "what are typical inputs?"
* Guiding Principle #2: don't pay much attention to constant factors, lower-order terms
   * justifications:
      * easier mathematically
      * constants depend on architecture / compiler / programmer any way
      * lose very little predictive power
   * can still be important for some optimizations
* Guiding Principle #3: asymptotic analysis: focus on running time for large input sizes n, as n tends toward infinity
   * justification: only big problems are interesting (sorting 100 numbers is fast regardless of method)
   * Moore's law does not negate this

* fast algorithm: worst-case running time grows slowly with input size
   * sweet spot: mathematical tractability and predictive power
   * ideally: linear running time
   
II. Asymptotic Analysis
-----------------------

* Asymtotic analysis: suppress constant factors and lower-order terms  
   * constant factors: too system-dependent  
   * lower-order terms: irrelevant for large inputs  
* example: 6n x logbase2(n) + 6n can be reduced to nlog(n), i.e. O(nlog(n))  
* searching an array of length n for t: O(n)  
* searching two arrays of length n for t: O(n)  
* searching two arrays for a common number n: O(n^2)  
* searching one array for a duplicate number n: O(n^2)

### Video: Big-Oh Notation
𝛰 (omicron)  
* for a function go be O(f(n)), eventually, for all sufficiently large values of n, it's bounded above by a constant multiple of f(n)
   * T(n) = O(f(n)) iff there exist constants c, n0 > 0 such that T(n) <= c*f(n) for all n >= n0  
   * c is the "constant multiple"  
   * n0 defines "sufficiently large"  
   * constants are independent of n
* Omega: T(n) >= c*f(n) for all n >= n0
* Theta: T(n) = 𝛳(f(n)) if and only if T(n) = O(f(n)) and T(n) = 𝛺(f(n))
* little-oh: "<" rather than "<="; harder to show b/c must be true for all c > 0
* little-omega: ">" rather than ">="

Problem Set #1
--------------
k-way-Merge Sort. Suppose you are given *k* sorted arrays, each with *n* elements, and you want to combine them into a 
single array of *kn* elements. Consider the following approach. Using the merge subroutine taught in lecture, you 
merge the first 2 arrays, then merge the 3rd given array with this merged version of the first two arrays, 
then merge the 4th given array with the merged version of the first three arrays, and so on until you merge 
in the final (*kth*) input array. What is the running time taken by this successive merging algorithm, as a 
function of *k* and *n*? (Optional: can you think of a faster way to do the k-way merge procedure?)

III. Divide & Conquer Algorithms
--------------------------------

### Video: O(n log n) Algorithm for Counting Inversions I

#### The Divide and Conquer Paradigm  
1. DIVIDE into smaller subproblems  
2. CONQUER via recursive calls  
3. COMBINE solutions of subproblems into one for the original problem  

#### Inversion Problem
In an array A containing 1,2,3,...,n in arbitrary order, how many times does A[i] > A[j] occur with i<j? (not just immediately adjacent!)  
* (1,3,5,2,4,6) has three inversions: 5,2; 3,2; 5,4
* crossing line segments between dots correspond to number of inversions
* why solve? numerical similarity measure between two ranked lists, "collaborative filtering" (like purchase histories)  
* in general, number of possible inversions is **n choose 2**  

Solving the problem:  
* could do a brute-force approach, double for-loop, but O(n^2) time (also, look at quadratic nature of **n choose 2**)  
* better: divide & conquer
* three types of inversions:  
   * **left** if i,j <= n/2  (can compute recursively)  
   * **right** if i,j > n/2  (can compute recursively)  
   * **split** if i<= n/2 < j (need separate subroutine for these)  
* approach: if n=1, return 0; else x=count(1st half), y=count(2nd half), z=countSplitInv(all); return x + y + z
   * implement countSplitInv in linear time O(n) - (then it will run in O(n log n) time overall, log n for the splitting arrays in half)  
   * in the case of (8,7,6,5,4,3,2,1), we want to count a quadratic number of thing in linear time!  

### Video: O(n log n) Algorithm for Counting Inversions II

#### Details
* piggyback on merge sort, which also runs in O(n log n) time  
* change to high-level: count will now be countAndSort, so each recursive call also returns a sorted array, and countSplitInv merges  
* if we have (1,3,5) B and (2,4,6) C, then when we copy the 2 to array D, we notice that it's smaller than each of the remaining elements in B  
* claim: the split inversions involving an element y of the array C are the numbers left in array B when y is copied to D  
   * (1) if x is copied to D before y, then x < y --> no split inversion; proof:  
   * (2) if y cipied to D before x, then y < x --> split inversion  
* to do this:  
   * while merging sorted subarrays, keep running total of number of split inversions  
   * when element from C gets copied to D, increment total by number of elements remaining in B  
* run time of this subroutine: O(n) (merge) + O(n) (running count) = O(n) (because we're not adding too many O(n)s!)  
   * total: O(n log n)  

### Video: Strassen's Subcubic Matrix Multiplication Algorithm
* idea: starting with an n x n matrix X, break into smaller matrices (quadrants or blocks, n/2 x n/2 matrices)  
   * blocks behave atomically  

#### Recursive Algorithm #1
* Step 1: recursively compute the 8 necessary products  
* Step 2: do the necessary additions (O(n^2)) time  
* running time (not obvious): with this kind of recursive algorithm where you do eight recursive calls, each on a problem with 
dimension half as much as what you started with, and then do quadratic time outside, the running time is going to be cubic (follows from master method)

#### Strassen's Algorithm (1969)
* Step 1: recursively compute only 7 (cleverly chosen) products  
   * this is better than it looks, since we save a recursive call repeatedly  
* Step 2: do the necessary (clever) additions and subtractions (still O(n^2) time)  
* better than cubic time  
* blew people's minds at the time b/c it was thought that all of the calculations needed to be done  
* how did he come up with this? "Honestly, your guess is as good as mine."
 
### Video: O(n log n) Algorithm for Closest Pair I \[Advanced - Optional\]  

#### Initial Observations
* brute-force search runs in O(n^2) time  
* 1-D version of problem:  
   * Step 1: sort points (O(n log n)time)  
   * Step 2: return closest pair of adjacent points (O(n) time)  
   * even on the line, there are a quadratic number of different pairs  
* goal: O(n log n) time algorithm for 2-D version  

#### High-Level Approach
* Step 1: make copies of points sorted by x-coordinate and y-coordinate (O(n log n) time) - it doesn't hurt our goal, so why not?
   * sorting is a primitive  
* Step 2: use Divide and Conquer

IV. The Master Method
---------------------

V. Quicksort - Algorithm
------------------------

### Video: Choosing a Good Pivot
* choosing the first element of an already sorted list results in 𝛳(n^2) running time (bad)
   * why? `>= n + (n - 1) + (n - 2) + ... + 1`  means first n/2 terms are all at least n/2
* choosing the median element results in 𝛳(n log n) running time (ideal)
   * (1) even a 25-75% split will achieve this
   * (2) we don't even have to be very lucky to get that kind of split (50% probability)
  
Quick Sort Theorem: for every input array of length n, the **average** running time of Quick Sort with random pivots is O(n log n)
* holds for every input  
* "average" depends on random choices made by the algorithm  

VI. Quicksort - Analysis
------------------------

### Video: Analysis I: A Decomposition Principle
**indicator variables** take on values of 0 or 1 to indicate whether a particular event happened (Xij in this case)  


### Video: Analysis II: The Key Insight

### Video: Analysis III: Final Calculations