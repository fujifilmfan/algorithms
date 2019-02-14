Divide and Conquer, Sorting and Searching, and Randomized Algorithms, Stanford University (via Coursera)
========================================================================================================

Course Contents and Repository Files
------------------------------------

### Week 1
----
#### Topics Covered
I. Introduction  
* Integer multiplication  
* Karatsuba multiplication  
* Merge Sort  
* Guiding principles for algorithm analysis  

II. Asymptotic Analysis  
* Big-oh notation  
* Big omega and theta

#### Programming Assignment
* **1-karatsuba.py** - implementation of Karatsuba multiplication  
   * I was a bit disappointed that I had to use string functions because I couldn't get the math functions to work out - something to revisit again  

### Week 2
----
#### Topics Covered
III. Divide & Conquer Algorithms  
* Counting inversions  
* Strassen's subcubic matrix multiplication algorithm  
* O(n log n) algorithm for closest pair  

IV. The Master Method  
* The master method formal statement, three cases, examples, and proofs  

#### Programming Assignment
* **2-merge_sort.py** - I figured it was best to implement the basic Merge Sort before attempting the problem set  
* **2-count_inversions.py** - counts the number of inversions (larger numbers appearing before smaller numbers) in a large array  
* **2-IntegerArray.txt** - array input for 2-count_inversions.py  

### Week 3
----
#### Topics Covered
V. Quicksort - Algorithm
* Quick sort  
* Partitioning around a pivot  

VI. Quicksort - Analysis
* A decomposition principle  

VII. Probability Review

#### Programming Assignment

* **3-quick_sort-first_element_pivot.py** - Quick Sort using first element of array as pivot
* **3-quick_sort-last_element_pivot.py** - Quick Sort using last element of array as pivot
* **3-quick_sort-median_element_pivot.py** - Quick Sort using a median as the pivot element
* **3-QuickSort.txt** - array input for the 3-quick_sort-*.py scripts

### Week 4
----
#### Topics Covered
VIII. Linear-time Selection
* Randomized selection  
* Deterministic selection  
* Omega(n log n) lower bound for comparison-based sorting  

IX. Graphs and the Contraction Algorithm
* Graphs and minimum cuts  
* Graph representations (adjacency matrix vs. adjacency list)  
* Random contraction algorithm  
* Counting minimum cuts  

#### Programming Assignment

* **4-karger_min_cut.py** - determines the minimum number of edges to cut in a connected graph in order to separate it into two parts  
  * success rate is only about 1%  
  * takes about 150s to run 1000 trials (file I/O is slow)  
* **4-kargerMinCut.txt** - array input for 4-karger_min_cut.py  

### Other
----
* **Algorithms-course_notes.md** - notes on the Coursera course  
* **Algorithms-book_notes.md** - notes on the Algorithms book by Dasgupta, Papadimitriou, and Vazirani  
* **function_plots.gcx** - lots of function plots for Apple's Grapher application  
* I finished!  Here's how to cite the course: "Divide and Conquer, Sorting and Searching, and Randomized Algorithms by Stanford University on Coursera. Certificate earned at Thursday, February 14, 2019 4:15 AM GMT".
