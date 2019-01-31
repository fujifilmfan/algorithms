Algorithms
==========
Dasgupta, Papadimitriou, and Vazirani
-------------------------------------

### Chapter 0: Prologue

#### 0.2 Enter Fibonacci
Whenever we have an algorithm, there are three questions we always ask about it:  
1. Is it correct?
2. How much time does it take, as a function of n?
3. And can we do better?

#### 0.3 Big-O notation
Definition:  
Let f(n) and g(n) be functions from positive integers to positive reals. We say f = O(g) (which means that  
“f grows no faster than g”) if there is a constant c > 0 such that f(n) ≤ c · g(n).


Here are some commonsense rules that help simplify functions by omitting dominated terms:  
1. Multiplicative constants can be omitted: 14n^2 becomes n^2.
2. n^a dominates n^b if a > b: for instance, n^2 dominates n.
3. Any exponential dominates any polynomial: 3^n dominates n^5 (it even dominates 2^n).
4. Likewise, any polynomial dominates any logarithm: n dominates (log n)^3 . This also means, for example, that n^2 dominates n log n.

O(1) < O(log n) < O( Sqrt(n) ) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n)