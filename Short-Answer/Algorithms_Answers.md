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
Some preliminary minor questions I had:
- Do I have to factor or take into consideration going up and down the stairs to the ground floor to verify that the egg is broken? 
- How am I traveling between the floors? Whether I have to take the stairs or I am allowed to take the elevator?

Assuming that traveling between the floors and verifying if eggs are broken is trivial, my first pass solution for this problem would be to employ a sort of modified binary search approach: 
- The floors of a building in some sense constitute an ordered list (the third floor must come before the 15th floor). 
- Binary search is used as a quick means of guessing a number chosen from a list of possible numbers and guessing which is the minimum floor f at which an egg would not be broken, anything below f is assumed safe. 

Here are the steps:
- I would find "the middle floor" of the building (that is what is the midpoint, e.g. around 5th floor for 10-story building). 
- I would then drop an egg off this floor.
- If egg breaks, I would divide the remaining floors in half (e.g. if egg breaks at 5 in ten story building, go to floor 3) and go to the new "middle floor" and start testing there and so on and so on dividing in half each subsequent test if the eggs continue breaking 
- One thing to watch out for would be if the egg did not break (e.g. if egg does not break at 3rd floor, it's possible it would still not break at fourth floor; it would obviously not break at anything below 3) 

Worst case we are looking at O(log n) but best case is O(1); average case is also O(log n)

