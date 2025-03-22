# Monotonic Stack

Knowledge from: https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems

## Problem

Monotonic stacks are generally used for solving questions of the type -

- next greater element
- next smaller element
- previous greater element
- previous smaller element

## Four types of Monotonic Stack

1. Strictly increasing
   - every element of the stack is strictly greater than the previous element. Example - [1, 4, 5, 8, 9]
2. Non-decreasing
   - every element of the stack is greater than or equal to the previous element. Example - [1, 4, 5, 5, 8, 9, 9]
3. Strictly decreasing
   - every element of the stack is strictly smaller than the previous element - [9, 8, 5, 4, 1]
4. Non-increasing
   - every element of the stack is smaller than or equal to the previous element. - [9, 9, 8, 5, 5, 4, 1]

## A generic template

We can use the following template to build a stack that keep the monotonous property alive through the execution of the program.

```python
def build_mono_stack(arr):
    # Initialize an empty stack
    stack = []

    # Iterate through all elements in the array
    for i in range(len(arr)):
        # While stack is not empty and the element represented by stack top OPERATOR arr[i]
        # OPERATOR could be >, <, >=, <= depending on whether you want increasing or decreasing stack
        while stack and arr[stack[-1]] > arr[i]:  # Example: for next smaller element
            # Pop the top element
            stack_top = stack.pop()

            # Do something with stack_top here
            # For example: next_smaller[stack_top] = i

        if stack:
            # If stack has some elements left
            # Do something with stack top here
            # For example: previous_smaller[i] = stack[-1]

        # At the end, push the current index into the stack
        stack.append(i)

    # At all points in time, the stack maintains its monotonic property
    return stack  # Or return any result arrays you've built
```

## Notes about the template above

1. We initialize an empty stack at the beginning.
2. The stack contains the index of items in the array, not the items themselves
3. There is an outer for loop and inner while loop.
4. At the beginning of the program, the stack is empty, so we don't enter the while loop at first.
5. The earliest we can enter the while loop body is during the second iteration of for loop. That's when there is at least an item in the stack.
6. At the end of the while loop, the index of the current element is pushed into the stack
7. The OPERATOR inside the while loop condition decides what type of monotonic stack are we creating.
8. The OPERATOR could be any of the four - >, >=, <, <=

## Time complexity

It can be argued that no element is accessed more than four times (a constant) - one, when comparing its value with the item in the stack (while conditional). two, when pushing the item in the stack. three, when comparing this item in the stack with the current item being iterated (while conditional again). four, when popping the item out of stack. As a result, the time complexity of this algorithm is linear. - **O(n)** where n is the number of elements in the array.

## Space complexity

Because we are using an external data structure - stack. In the worst can it can be filled with all the elements in the array. The space complexity is also linear. - **O(n)** where n is the number of elements in the array.

## When to use monotone increasing vs monotone decreasing?

In our implementation, finding next greater and previous greater elements require building a monotone decreasing stack. For finding next smaller and previous smaller requires building a monotone increasing stack. To help you remember this, think of this as an inverse relation - **greater requires decreasing/non-increasing, smaller requires increasing/non-decreasing stacks**.

### 1. Next Greater

We are given with the following array and we need to find the next greater elements for each of items of the array.

`arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]`

Next greater elements (what is the next greater element for the item at this index) -

`nextGreaterElements = [null, 9, 5, 9, 5, 9, 12, 12, 12, null]`

On the place of writing the element itself, we can also write its index -

`nextGreaterIndexes = [-1, 6, 3, 6, 5, 6, 9, 9, 9, -1]`

Let's use the template given above to solve this question. The following code uses the template and implement next greater element program. Please read the comments in the code to understand what we are doing on these lines.

```python
def find_next_greater_indexes(arr):
    # initialize an empty stack
    stack = []

    # initialize nextGreater array, this array holds the output
    # initialize all the elements as -1 (invalid value)
    next_greater = [-1] * len(arr)

    # iterate through all the elements of the array
    for i in range(len(arr)):

        # while loop runs until the stack is not empty AND
        # the element represented by stack top is STRICTLY SMALLER than the current element
        # This means, the stack will always be monotonic non increasing (type 4)
        while stack and arr[stack[-1]] < arr[i]:

            # pop out the top of the stack, it represents the index of the item
            stack_top = stack.pop()

            # as given in the condition of the while loop above,
            # nextGreater element of stackTop is the element at index i
            next_greater[stack_top] = i

        # push the current index
        stack.append(i)

    return next_greater
```

**Notes**

1. For finding next greater elements (not equal) we use a monotonic non increasing stack (type 4)

2. If the question was to find next greater or equal elements, then we would have used a monotonic strictly decreasing stack (type 3)

3. We use the operator < in while loop condition above - this results in a monotonic non increasing stack (type 4). If we use <= operator, then this becomes a monotonic strictly decreasing stack (type 3)

4. Time and space complexity - O(n)

### 2. Previous Greater

This time we want to find the previous greater elements. One option is to iterate from arr.length - 1 to 0 and use the same logic as above in the opposite direction. In order to keep things simple, I rather like another flavour of the template above where we add three more lines after the while loop to get the previous greater element. Let's see how to do that.

`arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]`

`previous_greater_elements = [None, 13, 8, 8, 5, 8, 13, 9, 7, 13]`

`previous_greater_indexes = [-1, 0, 1, 1, 3, 1, 0, 6, 7, 0]`

```python
def find_previous_greater_indexes(arr):
    # initialize an empty stack
    stack = []

    # initialize previousGreater array, this array holds the output
    # initialize all the elements as -1 (invalid value)
    previous_greater = [-1] * len(arr)

    # iterate through all the elements of the array
    for i in range(len(arr)):

        # while loop runs until the stack is not empty AND
        # the element represented by stack top is SMALLER OR EQUAL to the current element
        # This means, the stack will always be strictly decreasing (type 3) - because elements are popped when they are equal
        # so equal elements will never stay in the stack (definition of strictly decreasing stack)
        while stack and arr[stack[-1]] <= arr[i]:

            # pop out the top of the stack, it represents the index of the item
            stack_top = stack.pop()

        # after the while loop, only the elements which are greater than the current element are left in stack
        # this means we can confidently decide the previous greater element of the current element i, that's stack top
        if stack:
            previous_greater[i] = stack[-1]

        # push the current element
        stack.append(i)

    return previous_greater
```

**Notes**

1. For finding previous greater elements (not equal) we use a monotonic strictly decreasing stack (type 3)

2. If the question was to find previous greater or equal elements, then we would have used a monotonic non increasing stack (type 4)

3. We use the operator <= in while loop condition above - this results in a monotonic strictly decreasing stack (type 3). If we use < operator, then this becomes a monotonic non increasing stack (type 4).

4. Time and space complexity - O(n)

### 3. Next Greater and Previous Smaller at the same time

If we merge the code from heading (1) and (2) both above, we can get next greater and previous greater from the same program. There is only one limitation.

One of previousGreater or nextGreater won't be strictly greater (but greater or equal). If this satisfies our requirement, we can use the following solution.

For example, in the array `[13, 8, 1, 5, 2, 5, 9, 7, 6, 12]`

The next greater element for the first 5 will be 9, the previous greater element for the second 5 will be 5 (not 8)

OR

The next greater element for the first 5 will be 5 (not 9), the previous greater element for the second 5 will be 8.

This solution works if you are okay with one of the two cases above. Let's look at the code now.

```python
def find_next_and_previous_greater_indexes(arr):
    # initialize an empty stack
    stack = []

    # initialize previousGreater and nextGreater arrays
    previous_greater = [-1] * len(arr)
    next_greater = [-1] * len(arr)

    # iterate through all the elements of the array
    for i in range(len(arr)):

        # while loop runs until the stack is not empty AND
        # the element represented by stack top is SMALLER OR EQUAL to the current element
        # This means, the stack will always be strictly decreasing (type 3) - because elements are popped when they are equal
        # so equal elements will never stay in the stack (definition of strictly decreasing stack)
        while stack and arr[stack[-1]] <= arr[i]:

            # pop out the top of the stack, it represents the index of the item
            stack_top = stack.pop()

            # This is the only additional line added to the last approach
            # decides the next greater element for the index popped out from stack
            next_greater[stack_top] = i

        # after the while loop, only the elements which are greater than the current element are left in stack
        # this means we can confidently decide the previous greater element of the current element i, that's stack top
        if stack:
            previous_greater[i] = stack[-1]

        # push the current element
        stack.append(i)

    return [previous_greater, next_greater]
```

### Next Smaller (strictly smaller)

To get previous greater elements we simply flip the operator from < to >. By doing this we end up creating a strictly increasing (type 1) or a non-decreasing (type 2) array.

```python
def findNextSmallerIndexes(arr):
    # initialize an empty stack
    stack = []

    # initialize nextGreater array, this array hold the output
    # initialize all the elements are -1 (invalid value)
    nextSmaller = [-1] * len(arr)

    # iterate through all the elements of the array
    for i in range(len(arr)):

        # while loop runs until the stack is not empty AND
        # the element represented by stack top is STRICTLY LARGER than the current element
        # This means, the stack will always be monotonic non decreasing (type 2)
        while stack and arr[stack[-1]] > arr[i]:

            # pop out the top of the stack, it represents the index of the item
            stackTop = stack.pop()

            # as given in the condition of the while loop above,
            # nextSmaller element of stackTop is the element at index i
            nextSmaller[stackTop] = i

        # push the current element
        stack.append(i)

    return nextSmaller
```

### Previous Smaller (strictly smaller)

```python
def findNextSmallerIndexes(arr):
  # initialize an empty stack
  stack = []

  # initialize previousSmaller array, this array hold the output
  # initialize all the elements are -1 (invalid value)
  previousSmaller = [-1] * len(arr)

  # iterate through all the elements of the array
  for i in range(len(arr)):

    # while loop runs until the stack is not empty AND
    # the element represented by stack top is LARGER OR EQUAL to the current element
    # This means, the stack will always be monotonic strictly increasing (type 1)
    while stack and arr[stack[-1]] >= arr[i]:

      # pop out the top of the stack, it represents the index of the item
      stackTop = stack.pop()

    # this is the additional bit here
    if stack:
      # the index at the stack top refers to the previous smaller element for `i`th index
      previousSmaller[i] = stack[-1]

    # push the current element
    stack.append(i)

  return previousSmaller
```

### 6. Next Smaller and Previous Smaller merged (one strictly smaller, and the other smaller or equal)

```python
def find_next_and_previous_smaller_indexes(arr):
    # initialize an empty stack
    stack = []

    # initialize nextSmaller array for output
    next_smaller = [-1] * len(arr)

    # initialize previousSmaller array, this array holds the output
    # initialize all the elements as -1 (invalid value)
    previous_smaller = [-1] * len(arr)

    # iterate through all the elements of the array
    for i in range(len(arr)):

        # while loop runs until the stack is not empty AND
        # the element represented by stack top is LARGER OR EQUAL to the current element
        # This means, the stack will always be monotonic strictly increasing (type 1)
        while stack and arr[stack[-1]] >= arr[i]:

            # pop out the top of the stack, it represents the index of the item
            stack_top = stack.pop()

            # as given in the condition of the while loop above,
            # nextSmaller element of stackTop is the element at index i
            next_smaller[stack_top] = i

        # this is the additional bit here
        if stack:
            # the index at the stack top refers to the previous smaller element for `i`th index
            previous_smaller[i] = stack[-1]

        # push the current element
        stack.append(i)

    return [next_smaller, previous_smaller]
```

## Summary

| Problem          | Stack Type                 | Operator in while loop | Assignment Position |
| ---------------- | -------------------------- | ---------------------- | ------------------- |
| next greater     | decreasing (equal allowed) | stackTop < current     | inside while loop   |
| previous greater | decreasing (strict)        | stackTop <= current    | outside while loop  |
| next smaller     | increasing (equal allowed) | stackTop > current     | inside while loop   |
| previous smaller | increasing (strict)        | stackTop >= current    | outside while loop  |
