
--- 

There are two types of exercise in this course:

- autograded
- exploratory *(optional)*

**You are expected to complete all of the autograded exercises**, as these are the only ones that will be checked by the autograder and reviewed by the TA. **Exploratory exercises (or "explorations") are optional**, and responses for these will only be reviewed upon request.

Only update the files listed in the exercises themselves. Changing any other file may affect your autograder feedback.

---

# autograded exercises

For these exercises, add your functions to the *apputil\.py* file. If you like, you're welcome to adjust the *app\.py* file, but it is not required. The autograder will only check the *apputil\.py* file.

## exercise 1

Given enough pennies (1 cent) and nickels (5 cents), write a function `ways(n)` which calculates the number of ways you can make change for a given amount of cents `n`. The function should return the number of ways to yield `n` cents using only pennies and nickels.

**Test Cases:**

```python
function   --->      (num pennies, num nickels)
    
ways(12)   ---> 3    [(2, 2), (7, 1), (12, 0)]               
ways(20)   ---> 5    [(0, 4), (5, 3), (10, 2), (15, 1), (20, 0)]
ways(3)    ---> 1    [(3, 0)]
ways(0)    ---> 1    [(0, 0)]
```

*Note: the autograder will be checking only for the function to return the **number** of ways. The items listed to the right, above, are for reference only.*

## exercise 2

Suppose we have student `names`, and test `scores` for each student, respectively. For example, we could have:

```python
names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])
```

### part 1

Use NumPy to write a function `lowest_score(names, scores)` that returns the `name` of the student with the lowest `score`.

> Hint: take a look at the [argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html) function.

### part 2

Write a similar function `sort_names(names, scores)` that will list the names of students in *descending* order of test score (i.e., a list of names, with associated scores in order from highest to lowest).

---

# exploratory exercises

For these explorations, add your functions to the *apputil\.py* file. If you like, you can also explore Streamlit by incorporating functions into the *app\.py* file.

*Note: the following explorations are completely optional.*

## exploration 1

- Let `s` be a 1-D boolean (True/False) NumPy array where each element represents a student, and each value is an indicator for whether a student was caught texting in class.
- Let `d` be 1-D numeric array where each element represents an instructor, and each value is the number of points that instructor would remove from a student's grade if they are caught texting in class.

### part 1

Write a function which takes in `s` and `d`, and returns an array with a row for each instructor, and a column for each student. The values should be the number of points that would be removed for each student-instructor combination.

**Example:**

```python
s = np.array([True, False, False, True, True])
d = np.array([20, 15])

>>> text_removals(s, d)
>>> array([[20,  0,  0, 20, 20],
           [15,  0,  0, 15, 15]])
```

### part 2

Adjust the function to return the total number of points each instructor would have removed by adding an *optional* Boolean argument called `totals`.

**Example:**

```python
s = np.array([True, False, False, True, True])
d = np.array([20, 15])

>>> text_removals(s, d, totals=True)
>>> array([60, 45])
```

## exploration 2

Update your `ways` function to incorporate an *arbitrary* set of coin values. I.e., your function should now look something like this:

```python
def ways(cents, coin_types=[1, 5]):
    # code code ...

>>> ways(100, [25, 10, 5, 1])
>>> 242
```
