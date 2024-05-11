
# Remove Elements

## Hey! Leetcode Question 2:-
## Code
```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = nums.count(val)
        for i in range(p):
            nums.remove(val)
        print(nums)
```


## What I learn from this question:-

In this question, I first count the duplicate elements which mention in question named as "var" then I ran a loop within the range of dupilcate count and remove those variable elements.



Used Theory here:-
    1.remove = python list remove() Method
   ### * The worst part for me was the removal element,that as it only remove the single elements , and that too the first occurence.
