# bubbling-zeroes-problem
Given an integer array, move all zeros present in it to the end. The solution should maintain the relative order of items in the array.

INTRODUCTION :
We will use two indexes :
  1)  1 for finding the index of value '0'. We will call it zero_finder.
  2)  Another for finding the index of a non-zero value to swap with the '0'. We will call it swapper for simpler terminology.
  
      This value will be copied directly to zero_finder's value removing the need for a temporary value and set it to 0.
      
      Since, the zeroes areto be shifted to the right of the array, this value will always be greater than zero_finder.
  The two indexes will not be the same.

STEP 1 : Initialise the two indexes to the start of the array. (both will start from index=0)

STEP 2 : Start finding the right values for the two indexes. (iterative method to be used - here we iterated swapper)

STEP 3 : If value at swapper is '0' - increment, else we use this index for swapping.
         If Value at zer_finder is non-zero - increment, else we use this index for swapping.
         
STEP 4 : After swapping, both indexes are incremented by 1.
