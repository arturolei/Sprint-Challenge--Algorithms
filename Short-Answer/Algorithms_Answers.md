#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
```python
    a = 0
    while (a < n * n * n):
      a = a + n * n
```

The runtime of this is O(n). 
The initial assignment `a=0` has runtime of O(c), and can be discarded in relation to the higher power term which in this case would be the `while` loop:
```python
  while (a < n * n * n):
      a = a + n * n
```
Although the `while` loop grows by more than `a` each run through, it really is determined by size of `n` because of `n*n*n` and thus for sufficiently large `n`; this loop will be O(n)


b) O(n log n) - linearithmic
```python
sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
As n gets bigger, the outer loop will take same amount of time every pass  as i increments by 1(and approaches O(n)), but the second inner `while` loop is dependent on an a parameter `j` that is incremented by more than 1, thus the second inner loop is logarithmic, and thus we have (given assignment at program/code snippet start): `O(1) + O(n * log(n))` which simplifies to O(n*log n)

c) O(n)
```python
def bunnyEars(bunnies):
    if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
This is a recursive function, so we can perhaps assume that the total running time is sum of each of recursive call; each recursive call either results in an addition of `0` or another additive operation (another `2` being added to the sum). 



## Exercise II
Question:
```
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
```

